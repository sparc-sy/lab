---
title: "AS5600 — مشفر مغناطيسي (Magnetic Encoder)"
weight: 5
description: "مشفر زاوية مغناطيسي من ams OSRAM يعمل مع مغناطيس ثنائي القطب."
image: "images/encoder.jpg"
---

مشفر زاوية مغناطيسي من ams OSRAM، يعمل مع مغناطيس ثنائي القطب على المحور. يوفر زاوية مطلقة 0°–360° (قابلة للضبط حتى 18°) عبر I2C أو خرج تناظري/ PWM.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| الجهد | 3.0 V – 5.5 V (VDD3V3 أو VDD5V) |
| الاستهلاك | 6.5 mA typ. |
| الدقة | 12-bit (4096 خطوة/دورة) |
| واجهات الخرج | I2C، تناظري (نسبي لـ VDD)، PWM |
| عنوان I2C | 0x36 (افتراضي، برمجة) |
| درجة الحرارة | -40 °C إلى +125 °C |

## أمثلة الاستخدام

- استخدام **AS5600** مع Arduino: قراءة السجل 0x0C (ANGLE) عبر I2C أو مكتبة Adafruit_AS5600.
- مع Raspberry Pi: استخدام `smbus2` لقراءة الزاوية لربطها بمحرك أو ذراع روبوتي.
- ربط مغناطيس على عمود محرك وتثبيت AS5600 فوقه لقياس الزاوية المطلقة (تحكم بمحرك، عجلة، أو مفصل).

## روابط مفيدة

- [الداتاشيت AS5600 (ams)](https://www.ams.com/en/products/position-sensors/magnetic-rotary-position-sensors/as5600)
- [Adafruit AS5600](https://www.adafruit.com/product/5557)
- [Adafruit AS5600 Library](https://github.com/adafruit/Adafruit_AS5600)
