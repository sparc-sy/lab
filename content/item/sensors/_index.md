---
title: "45 Sensors Modules Starter Kit — مجموعة مستشعرات لراسبيري باي"
weight: 6
description: "مجموعة تعليمية تحتوي على عشرات الموديولات مع دوائر مدمجة لـ Raspberry Pi."
image: "images/sensors.jpg"
---

مجموعة تعليمية تحتوي على عشرات الموديولات (حرارة، رطوبة، ضوء، حركة، غاز، صوت، لمس، إلخ) مع دوائر مدمجة وواجهة سهلة لـ Raspberry Pi.

## المواصفات التفصيلية

- عادة تشمل: مستشعر حرارة/رطوبة، LDR، PIR، مستشعر غاز، ميكروفون، زر، LED، ريليه، إلخ.
- التوافق: GPIO 3.3 V لراسبيري باي؛ بعض الموديولات تحتاج 5 V أو مقسم جهد.
- التوصيل: عادة عبر أسلاك أنثى-أنثى إلى رؤوس GPIO.

## أمثلة الاستخدام

- قراءة مستشعر DHT11/DHT22 من GPIO باستخدام مكتبة Python.
- توصيل مستشعرات I2C (مثل BME280) على SDA/SCL وقراءتها بـ `smbus2`.
- بناء لوحة تحكم بسيطة تعرض القراءات من عدة مستشعرات.

## روابط مفيدة

- [Raspberry Pi GPIO documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)
- [Raspberry Pi Sensor Tutorials](https://www.raspberrypi.com/documentation/computers/sensors.html)
- [Python GPIO Examples](https://github.com/gpiozero/gpiozero)
- [Sensor Kit Getting Started](https://github.com/kookye/Raspberry-Pi-Super-Starter-Kit)
