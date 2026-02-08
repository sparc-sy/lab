---
title: "LILYGO LoRa32 V2.1 — لوحة ESP32 مع LoRa"
weight: 14
description: "لوحة من LILYGO تجمع ESP32 مع موديول LoRa واختيارياً شاشة OLED."
image: "https://github.com/Xinyuan-LilyGO/LilyGo-LoRa-Series/raw/master/image/Lora32_v2.1.jpg"
---

لوحة من LILYGO تجمع ESP32 مع موديول LoRa (SX1276/SX1278) واختيارياً شاشة OLED.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| MCU | ESP32 (dual-core, Wi‑Fi, BLE) |
| LoRa | SX1276 أو SX1278 (868 / 915 MHz) |
| الجهد | 3.3 V (من USB 5 V عبر منظم) |
| الشاشة | OLED 0.96" (I2C) في بعض الطرازات |
| الواجهة | SPI (LoRa), I2C (OLED), GPIO |

## أمثلة الاستخدام

- استخدام مكتبة **RadioLib** أو **LoRa** مع Arduino لـ ESP32 لإرسال واستقبال حزم LoRa.
- ربط مع بوابة LoRaWAN (مثل The Things Network) وتسجيل الجهاز وإرسال بيانات المستشعرات.
- بناء شبكة نقطة–نقطة بين لوحتين لقياس المدى ومعدل فقدان الحزم.

## روابط مفيدة

- [Official Product Page (LILYGO TTGO LoRa32 v2)](https://github.com/Xinyuan-LilyGO/LilyGo-LoRa-Series/tree/master/TTGO%20LoRa32)
- **Datasheet:** لا توجد داتاشيت رسمية موحدة للوحة؛ يتم الرجوع إلى مخططات اللوحة وداتاشيت الشرائح المستخدمة.
- [Official Usage Docs (LILYGO LoRa Series Docs)](https://github.com/Xinyuan-LilyGO/LilyGo-LoRa-Series)
- [SDK Samples (LILYGO LoRa32 Examples)](https://github.com/Xinyuan-LilyGO/LilyGo-LoRa-Series/tree/master/examples)
