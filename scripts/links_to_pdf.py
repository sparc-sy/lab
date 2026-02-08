#!/usr/bin/env python3
"""
Generate a PDF from a links file: 4 items per page, each with QR code + title.
Reads items dynamically from the input file; fully scalable.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Optional deps - fail with clear message if missing
try:
    import qrcode
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.utils import ImageReader
except ImportError as e:
    print("Missing dependencies. Install with: pip install -r requirements.txt", file=sys.stderr)
    raise SystemExit(1) from e

try:
    import arabic_reshaper
    from bidi.algorithm import get_display
    _HAS_ARABIC = True
except ImportError:
    _HAS_ARABIC = False

# --- Configuration (override via CLI or keep defaults) ---
DEFAULT_INPUT = "links.txt"
DEFAULT_OUTPUT = "lab-links-qr.pdf"
ITEMS_PER_PAGE = 4
PAGE_SIZE = A4
MARGIN_MM = 22
CARD_PADDING_MM = 14
CARD_GAP_MM = 6
QR_SIZE_MM = 36
TITLE_FONT_SIZE = 10
TITLE_LINE_HEIGHT = 1.38
TITLE_LINES_MAX = 4
CARD_FILL = "#fafafa"
CARD_STROKE = "#e0e0e0"
ACCENT_COLOR = "#2563eb"
FONT_LATIN_ARABIC = "LabelFont"  # registered TTF with Latin + Arabic
IMAGE_BOTTOM_PADDING_MM = 2  # padding above card bottom
DEFAULT_IMAGES_DIR = "content/images"


def _slug_from_url(url: str) -> str | None:
    """Extract item slug from URL like .../item/tof/ or .../item/rpi5."""
    url = url.rstrip("/")
    if "/item/" in url:
        return url.split("/item/")[-1].split("/")[0].strip() or None
    return None


def _find_item_image(images_dir: Path, slug: str) -> Path | None:
    """Return path to image for slug (e.g. tof -> tof.jpg or tof.png), or None."""
    if not slug or not images_dir.exists():
        return None
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        p = images_dir / f"{slug}{ext}"
        if p.exists():
            return p
    # Fallback: any file whose stem matches slug (case-insensitive)
    slug_lower = slug.lower()
    for f in images_dir.iterdir():
        if f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp") and f.stem.lower() == slug_lower:
            return f
    return None


def parse_links_file(path: Path) -> list[tuple[str, str]]:
    """
    Parse a links.txt-style file. Expects blocks of:
      - Title line (optional "—" separator)
      - Description line (skipped)
      - URL line (starts with https://)
    Returns list of (title, url).
    """
    text = path.read_text(encoding="utf-8")
    lines = [ln.rstrip() for ln in text.splitlines()]
    items: list[tuple[str, str]] = []
    i = 0

    while i < len(lines):
        line = lines[i]
        # Skip header / separator / footer
        if not line or line.startswith("==") or line.startswith("Total ") or line.startswith("Generated") or line.startswith("Website:"):
            i += 1
            continue
        # URL line: previous non-empty line was description, the one before that was title
        if line.startswith("https://"):
            url = line.strip()
            # Walk back to find title (first non-empty before description)
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            desc_idx = j  # description line
            j -= 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            title = lines[j].strip() if j >= 0 else "Item"
            # Keep full title (English + Arabic after " — ")
            items.append((title, url))
            i += 1
            continue
        i += 1

    return items


def _prepare_title_for_display(title: str) -> str:
    """Reshape Arabic and apply bidi for correct RTL/LTR display."""
    if not title or not _HAS_ARABIC:
        return title
    try:
        reshaped = arabic_reshaper.reshape(title)
        return get_display(reshaped)
    except Exception:
        return title


NOTO_ARABIC_URL = "https://github.com/google/fonts/raw/main/ofl/notosansarabic/NotoSansArabic-Regular.ttf"


def _download_noto_arabic(target: Path) -> bool:
    """Download Noto Sans Arabic to target path. Returns True on success."""
    import urllib.request
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        urllib.request.urlretrieve(NOTO_ARABIC_URL, target)
        return target.exists() and target.stat().st_size > 1000
    except Exception:
        return False


def _find_arabic_font() -> Path | None:
    """Return path to a TTF that supports Latin + Arabic, or None."""
    script_dir = Path(__file__).resolve().parent
    fonts_dir = script_dir / "fonts"
    noto_path = fonts_dir / "NotoSansArabic-Regular.ttf"
    candidates = [
        noto_path,
        Path("/Library/Fonts/Arial Unicode.ttf"),
        Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
        Path("/System/Library/Fonts/Supplemental/GeezaPro.ttf"),
        Path("/usr/share/fonts/truetype/noto/NotoSansArabic-Regular.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    for p in candidates:
        if p.exists():
            return p
    if _download_noto_arabic(noto_path):
        return noto_path
    return None


def _register_fonts(c: canvas.Canvas) -> bool:
    """Register a font with Arabic support. Returns True if Arabic-capable font is set."""
    font_path = _find_arabic_font()
    if font_path is None:
        return False
    try:
        pdfmetrics.registerFont(TTFont(FONT_LATIN_ARABIC, str(font_path)))
        return True
    except Exception:
        return False


def make_qr_image(url: str, size_px: int) -> bytes:
    """Generate QR code as PNG bytes."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # Resize to desired pixel size (img is a PIL Image)
    img = img.resize((size_px, size_px))
    from io import BytesIO
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def _wrap_title(c: canvas.Canvas, title: str, width: float, font_name: str, font_size: int, max_lines: int) -> list[str]:
    """Split title into lines that fit in width. Returns list of display-ready strings."""
    display_title = _prepare_title_for_display(title)
    words = display_title.split()
    lines: list[str] = []
    current: list[str] = []
    for w in words:
        test = " ".join(current + [w])
        if c.stringWidth(test, font_name, font_size) <= width:
            current.append(w)
        else:
            if current:
                lines.append(" ".join(current))
            current = [w] if c.stringWidth(w, font_name, font_size) <= width else [w[:1] + "…"]
    if current:
        lines.append(" ".join(current))
    out: list[str] = []
    for ln in lines[:max_lines]:
        if c.stringWidth(ln, font_name, font_size) > width:
            while ln and c.stringWidth(ln + "…", font_name, font_size) > width:
                ln = ln[:-1]
            ln = ln + "…"
        out.append(ln)
    return out


def draw_wrapped_title(
    c: canvas.Canvas,
    x: float,
    y: float,
    width: float,
    title: str,
    font_name: str,
    font_size: int = TITLE_FONT_SIZE,
    max_lines: int = TITLE_LINES_MAX,
    line_height: float = TITLE_LINE_HEIGHT,
) -> None:
    """Draw title with word wrap; uses font_name (supports Arabic when available)."""
    c.setFont(font_name, font_size)
    lines = _wrap_title(c, title, width, font_name, font_size, max_lines)
    line_pt = font_size * line_height
    for i, ln in enumerate(lines):
        c.drawString(x, y - i * line_pt, ln)


def _grid_for_items_per_page(n: int) -> tuple[int, int]:
    """Return (cols, rows) for given items per page (prefer more cols than rows)."""
    if n <= 0:
        return 1, 1
    import math
    r = int(math.ceil(math.sqrt(n)))
    c = (n + r - 1) // r
    return max(1, c), max(1, r)


def generate_pdf(
    items: list[tuple[str, str]],
    output_path: Path,
    *,
    items_per_page: int = ITEMS_PER_PAGE,
    margin_mm: float = MARGIN_MM,
    card_padding_mm: float = CARD_PADDING_MM,
    card_gap_mm: float = CARD_GAP_MM,
    qr_size_mm: float = QR_SIZE_MM,
    title_font_size: int = TITLE_FONT_SIZE,
    images_dir: Path | None = None,
    image_bottom_padding_mm: float = IMAGE_BOTTOM_PADDING_MM,
) -> None:
    """Build PDF with a grid of QR + title + item image cards (clean layout, Arabic support)."""
    cols, rows = _grid_for_items_per_page(items_per_page)
    gap = card_gap_mm * mm
    page_w, page_h = PAGE_SIZE
    margin = margin_mm * mm
    card_padding = card_padding_mm * mm
    qr_size_pt = qr_size_mm * mm
    image_bottom_pad = image_bottom_padding_mm * mm

    # Usable area: subtract margins and gaps between cards
    usable_w = page_w - 2 * margin - (cols - 1) * gap
    usable_h = page_h - 2 * margin - (rows - 1) * gap
    cell_w = usable_w / cols
    cell_h = usable_h / rows

    c = canvas.Canvas(str(output_path), pagesize=PAGE_SIZE)
    c.setTitle("SPARC Lab – Links QR")

    use_arabic_font = _register_fonts(c)
    font_name = FONT_LATIN_ARABIC if use_arabic_font else "Helvetica"
    if not use_arabic_font and _HAS_ARABIC:
        print("Note: No Arabic-capable font found; Arabic may not render. Add scripts/fonts/NotoSansArabic-Regular.ttf", file=sys.stderr)

    qr_size_px = int(qr_size_mm * (72 / 25.4))
    accent_h = 3  # points
    title_line_pt = title_font_size * TITLE_LINE_HEIGHT

    for page_start in range(0, len(items), items_per_page):
        page_items = items[page_start : page_start + items_per_page]
        for idx, (title, url) in enumerate(page_items):
            row = idx // cols
            col = idx % cols
            # Card rect (with gaps)
            card_x = margin + col * (cell_w + gap)
            card_y = page_h - margin - (row + 1) * (cell_h + gap) + gap
            card_w = cell_w
            card_h = cell_h

            # Card background and subtle border
            c.setFillColor(colors.HexColor(CARD_FILL))
            c.setStrokeColor(colors.HexColor(CARD_STROKE))
            c.setLineWidth(0.5)
            c.rect(card_x, card_y, card_w, card_h, fill=1, stroke=1)

            # Accent bar at top of card
            c.setFillColor(colors.HexColor(ACCENT_COLOR))
            c.rect(card_x, card_y + card_h - accent_h, card_w, accent_h, fill=1, stroke=0)
            c.setFillColor(colors.HexColor("#1f2937"))

            # Inner content area (below accent)
            inner_top = card_y + card_h - accent_h
            cx = card_x + card_padding
            cy = card_y + card_padding
            cell_inner_w = card_w - 2 * card_padding
            cell_inner_h = inner_top - card_y - 2 * card_padding

            # QR code centered horizontally, top of content area
            qr_img_bytes = make_qr_image(url, qr_size_px)
            from io import BytesIO
            qr_img = ImageReader(BytesIO(qr_img_bytes))
            qr_w, qr_h = qr_img.getSize()
            scale = min(qr_size_pt / qr_w, qr_size_pt / qr_h, cell_inner_w / qr_w, (cell_inner_h * 0.5) / qr_h)
            qr_draw_w, qr_draw_h = qr_w * scale, qr_h * scale
            qr_x = cx + (cell_inner_w - qr_draw_w) / 2
            qr_y = cy + cell_inner_h - qr_draw_h - 6
            c.drawImage(qr_img, qr_x, qr_y, width=qr_draw_w, height=qr_draw_h)

            # Title below QR
            title_y = qr_y - title_line_pt - 4
            title_lines = _wrap_title(c, title, cell_inner_w, font_name, title_font_size, TITLE_LINES_MAX)
            draw_wrapped_title(
                c, cx, title_y, cell_inner_w, title,
                font_name=font_name,
                font_size=title_font_size,
                max_lines=TITLE_LINES_MAX,
                line_height=TITLE_LINE_HEIGHT,
            )
            title_block_h = len(title_lines) * title_line_pt
            title_bottom = title_y - title_block_h

            # Item image: use all space under the title down to card bottom
            image_gap = 4
            image_top = title_bottom - image_gap
            image_bottom = cy + image_bottom_pad
            image_rect_h = image_top - image_bottom
            if images_dir and image_rect_h > 10:
                slug = _slug_from_url(url)
                img_path = _find_item_image(images_dir, slug) if slug else None
                if img_path:
                    try:
                        img = ImageReader(str(img_path))
                        iw, ih = img.getSize()
                        rw, rh = cell_inner_w, image_rect_h
                        scale_img = min(rw / iw, rh / ih)
                        dw, dh = iw * scale_img, ih * scale_img
                        dx = cx + (cell_inner_w - dw) / 2
                        dy = image_bottom + (image_rect_h - dh) / 2
                        c.drawImage(img, dx, dy, width=dw, height=dh)
                    except Exception:
                        pass

        c.showPage()

    c.save()


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate PDF with QR codes, titles, and item images from a links file.")
    parser.add_argument("input", nargs="?", default=DEFAULT_INPUT, help="Input links file (default: links.txt)")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT, help="Output PDF path")
    parser.add_argument("-n", "--per-page", type=int, default=ITEMS_PER_PAGE, help="Items per page (default: 4)")
    parser.add_argument("--margin-mm", type=float, default=MARGIN_MM, help="Page margin in mm")
    parser.add_argument("--qr-mm", type=float, default=QR_SIZE_MM, help="QR code size in mm")
    parser.add_argument("--images-dir", default=DEFAULT_IMAGES_DIR, help="Directory for item images (default: content/images)")
    parser.add_argument("--no-images", action="store_true", help="Do not include item images")
    args = parser.parse_args()

    base = Path(__file__).resolve().parent.parent
    input_path = Path(args.input) if Path(args.input).is_absolute() else base / args.input
    output_path = Path(args.output) if Path(args.output).is_absolute() else base / args.output
    images_dir = (Path(args.images_dir) if Path(args.images_dir).is_absolute() else base / args.images_dir) if not args.no_images else None

    if not input_path.exists():
        print(f"Error: input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    items = parse_links_file(input_path)
    if not items:
        print("No items found in input file.", file=sys.stderr)
        sys.exit(1)

    print(f"Parsed {len(items)} items from {input_path}")
    generate_pdf(
        items,
        output_path,
        items_per_page=args.per_page,
        margin_mm=args.margin_mm,
        qr_size_mm=args.qr_mm,
        images_dir=images_dir,
    )
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
