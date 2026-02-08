---
title: "VL53L0X — مستشعر ليزر لقياس المسافة (Time-of-Flight)"
weight: 1
description: "مستشعر قياس مسافة ليزري من STMicroelectronics يعتمد تقنية Time-of-Flight."
image: "images/tof.jpg"
---

مستشعر قياس مسافة ليزري من STMicroelectronics يعتمد تقنية Time-of-Flight. مناسب للمشاريع التعليمية والروبوتات وتطبيقات القياس القصير المدى.

## المواصفات التفصيلية (من الداتاشيت)


| المواصفة | القيمة |
|----------|--------|
| جهد التشغيل | 2.8 V – 3.3 V |
| استهلاك التيار | 19 mA (نشط)، ~1 µA (استعداد) |
| المدى | 30 mm – 2000 mm (حسب اللون والانعكاس) |
| دقة القياس | ±3% نموذجياً |
| واجهة الاتصال | I2C (400 kHz كحد أقصى) |
| عنوان I2C الافتراضي | 0x29 |
| الطول الموجي | 940 nm (ليزر VCSEL) |
| درجة حرارة التشغيل | -20 °C إلى 70 °C |

## أمثلة الاستخدام

- مكتبة **Adafruit_VL53L0X** لأردوينو: قراءة المسافة بالملليمتر.
- مع **Raspberry Pi**: استخدام `smbus2` وتهيئة الجهاز ثم قراءة المسافة في حلقة.
- قياس متعدد: استخدام XSHUT لتبديل عناوين I2C وتوصيل عدة مستشعرات على نفس الناقل.

## روابط مفيدة

- [الداتاشيت الرسمي (ST)](https://www.st.com/resource/en/datasheet/vl53l0x.pdf)
- [Adafruit VL53L0X](https://www.adafruit.com/product/3317)
- [Adafruit CircuitPython / Arduino library](https://github.com/adafruit/Adafruit_VL53L0X)
