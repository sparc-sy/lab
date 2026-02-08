---
title: "ESP32 UWB DW3000 (ESP32UWB3000) — Ultra Wideband"
weight: 13
description: "موديول ESP32 مع DW3000 من Qorvo لقياس المسافة والتموضع بدقة عالية."
image: "images/uwb.jpg"
---

موديول ESP32 مع DW3000 من Qorvo (IEEE 802.15.4z) لقياس المسافة والتموضع بدقة عالية، متوافق مع أنظمة FiRa.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| MCU | ESP32 |
| UWB | Qorvo DW3000 (IEEE 802.15.4z HRP) |
| المدى | حتى ~300 m (خط رؤية) |
| دقة المسافة | ~10 cm (TWR/TDoA)؛ زاوية ±5° مع PDoA |
| الواجهة | SPI بين ESP32 و DW3000 |
| التردد | 6.5 GHz (قنوات UWB)؛ حتى 6.8 Mbps |

## أمثلة الاستخدام

- استخدام **DW3000** مع ESP32 عبر مكتبات مثل `dw3000-esp` لتنفيذ Two-Way Ranging (TWR) بين جهازين.
- بناء نظام تموضع داخلي (indoor positioning) بعدة أنقرة (anchors) وعلامة (tag) لتتبع أصول أو أشخاص في مبنى.
- ربط النتائج مع تطبيق أو خادم لعرض المواقع على خريطة؛ أو استخدام المسافة الفورية لهبوط طائرة بدون طيار أو تفعيل أجهزة حسب الموقع.

## روابط مفيدة

- [Qorvo DW3000](https://www.qorvo.com/products/p/DW3000)
- [DW3000 Datasheet](https://www.qorvo.com/products/d/da000367)
- [ESP32 UWB / DW3000 community libraries (GitHub)](https://github.com/topics/dw3000)
