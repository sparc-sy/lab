---
title: "LILYGO LoRa32 V2.1 — لوحة ESP32 مع LoRa"
weight: 14
description: "لوحة من LILYGO تجمع ESP32 مع موديول LoRa واختيارياً شاشة OLED."
image: "images/lora.jpg"
---

لوحة من LILYGO تجمع ESP32 مع موديول LoRa (SX1276/SX1278) واختيارياً شاشة OLED، مناسبة لشبكات استشعار بعيدة المدى واستهلاك منخفض.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| MCU | ESP32 (dual-core، Wi‑Fi، BLE) |
| LoRa | SX1276 أو SX1278 (868 / 915 MHz) |
| الجهد | 3.3 V (من USB 5 V عبر منظم) |
| الشاشة | OLED 0.96" (I2C) في بعض الطرازات |
| الواجهة | SPI (LoRa)، I2C (OLED)، GPIO |

## أمثلة الاستخدام

- استخدام مكتبة **RadioLib** أو **LoRa** مع Arduino لـ ESP32 لإرسال واستقبال حزم LoRa (نقطة–نقطة أو شبكة).
- ربط مع بوابة LoRaWAN (The Things Network، ChirpStack) وتسجيل الجهاز وإرسال بيانات المستشعرات من الحقل أو المستودع.
- بناء عقدة استشعار بعيدة (رطوبة، حرارة، مستوى) مع عرض على OLED وإرسال دوري لتوفير البطارية.

## روابط مفيدة

- [LILYGO LoRa32 V2.1 Product Page](https://lilygo.cc/products/lora3)
- [LILYGO LoRa32 V2.1 Pinout & Specs](https://www.thethingsindustries.com/docs/hardware/devices/models/lilygo-lora32/)
- [LILYGO LoRa Series (GitHub)](https://github.com/Xinyuan-LilyGO/LilyGo-LoRa-Series)
- [RadioLib](https://github.com/jgromes/RadioLib)
- [The Things Network (LoRaWAN)](https://www.thethingsnetwork.org/)
