# مكونات المختبر — Lab Components Catalog

Source code for the university laboratory's public-facing component catalog, built with [Hugo](https://gohugo.io/).

The published website lists electronic components and devices available in the lab. Each item has a detailed web page and a printer-friendly summary.

## Quick Start

```bash
# Preview locally
hugo server

# Build for production
hugo --minify
```

Output goes to `public/`. Deploy its contents to any static-file host.

## Content Structure

```
content/
├── _index.md                          # Homepage
└── components/
    ├── _index.md                      # Component listing page
    └── <slug>/
        ├── _index.md                  # Detailed web page (front matter supports `image:`)
        └── print.md                   # Printer-friendly summary
```

## Theme

A custom `lab` theme lives in `themes/lab/` and ships with the repo (no submodules needed).

## Templates

Starter templates for new components are in `_templates/`:

| Template | Purpose |
|----------|---------|
| `web-template.md` | Full web page for a new component |
| `print-template.md` | Print-ready summary for a new component |

## Adding a New Component

1. Create `content/components/<slug>/`.
2. Copy `_templates/web-template.md` to `_index.md` inside that folder and fill in the details.
3. Copy `_templates/print-template.md` to `print.md` and fill in the summary.
4. Run `hugo server` to preview.

## License

MIT
