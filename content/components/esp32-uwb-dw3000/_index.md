---
title: "ESP32 UWB DW3000 (ESP32UWB3000) — Ultra Wideband"
weight: 13
description: "موديول ESP32 مع DW3000 من Qorvo لقياس المسافة والتموضع بدقة عالية."
image: "https://www.makerfabs.com/desfile/files/ESP32-UWB-2.jpg"
---

موديول ESP32 مع DW3000 من Qorvo لتقنية UWB لقياس المسافة والتموضع بدقة عالية.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| MCU | ESP32 |
| UWB | Qorvo DW3000 (IEEE 802.15.4z HRP) |
| المدى | حتى ~300 m (LOS) |
| دقة المسافة | ~10 cm |
| الواجهة | SPI بين ESP32 و DW3000 |
| التردد | 6.5 GHz (قنوات UWB) |

## أمثلة الاستخدام

- استخدام **DW3000** مع ESP32: مكتبات مثل `dw3000-esp` أو مثيلات من المجتمع لتنفيذ Two-Way Ranging (TWR).
- بناء نظام تموضع داخلي بعدة أنقرة (anchors) وعلامة (tag).
- ربط النتائج مع تطبيق أو خادم لعرض المواقع على خريطة.

## روابط مفيدة

- [Official Product Page (Qorvo DW3000)](https://www.qorvo.com/products/p/DW3000)
- [Datasheet (DW3000)](https://www.qorvo.com/products/d/da000367)
- [SDK Samples (Qorvo UWB Software)](https://www.qorvo.com/design-hub/design-tools/software)
