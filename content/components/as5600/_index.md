---
title: "AS5600 — مشفر مغناطيسي (Magnetic Encoder)"
weight: 5
description: "مشفر زاوية مغناطيسي من ams OSRAM يعمل مع مغناطيس ثنائي القطب."
image: "https://www.mouser.com/images/ams/images/AS5600-ASOM_SPL.jpg"
---

مشفر زاوية مغناطيسي من ams OSRAM، يعمل مع مغناطيس ثنائي القطب على المحور. يوفر زاوية مطلقة ودورات عبر I2C وتقنيات أخرى.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| الجهد | 3.0 V – 5.5 V |
| الاستهلاك | 6.5 mA typ. |
| الدقة | 12-bit (4096 خطوة/دورة) |
| واجهات الخرج | I2C, analog (0–VDD), PWM |
| عنوان I2C | 0x36 (برمجة) |
| درجة الحرارة | -40 °C إلى +125 °C |

## أمثلة الاستخدام

- استخدام **AS5600** مع Arduino: قراءة السجل 0x0C (ANGLE) عبر I2C.
- مع Raspberry Pi: استخدام `smbus2` لقراءة الزاوية.
- ربط مغناطيس على عمود المحرك وتركيب AS5600 فوقه لقياس الزاوية.

## روابط مفيدة

- [Official Product Page (AS5600)](https://ams-osram.com/products/sensors/position-sensors/ams-as5600-position-sensor)
- [Datasheet (AS5600 PDF)](https://look.ams-osram.com/m/7059eac7531a86fd/original/AS5600-DS000365.pdf)
- [Official Examples (Adafruit AS5600 Library)](https://github.com/adafruit/Adafruit_AS5600)
