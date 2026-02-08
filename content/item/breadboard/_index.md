---
title: "Breadboards و Wire Sets — لوحات تجارب وأسلاك"
weight: 16
description: "مجموعة لوحات تجارب وأطقم أسلاك للمختبر."
image: "images/breadboard.jpg"
---

مجموعة لوحات تجارب (breadboard) وأطقم أسلاك للمختبر: 5× 1660 نقطة، 20× 400 نقطة، 10× MB102، 10× طقم أسلاك (40 سلك لكل طقم).

## المواصفات التفصيلية

| النوع | الوصف التقريبي |
|-------|-----------------|
| Breadboard 1660-point | لوحة كبيرة، منافذ كافية لمشاريع معقدة؛ ثقوب متصلة داخلياً في صفوف (5 ثقوب) ومسارات تغذية على الجانبين. |
| Breadboard 400-point | لوحة متوسطة؛ نفس مبدأ التوصيل، أقل عدد ثقوب. |
| MB102 | لوحة تغذية (power supply module) توفر جهدين قابلين للضبط (مثلاً 3.3 V و 5 V) من مصدر خارجي؛ مناسبة لتغذية عدة دوائر على الـ breadboard. |
| Wire Set (40 wires) | أسلاك جاهزة (أنثى–أنثى أو ذكر–أنثى) بألوان مختلفة؛ مناسبة لـ GPIO وI2C وSPI والتغذية. |

**ملاحظة:** التيار المسموح عبر مجموعة ثقوب واحدة في الـ breadboard محدود (عادة 1 A أو أقل)； استخدم مصدر تغذية خارجي للمحركات والتيارات العالية.

## أمثلة الاستخدام

- توصيل Arduino Nano أو ESP32 على breadboard 400-point وتوصيل مستشعر عبر I2C (SDA, SCL, VCC, GND).
- استخدام MB102 لتغذية 3.3 V و 5 V لأجزاء مختلفة من الدائرة.
- بناء دائرة على 1660-point تجمع عدة مستشعرات ومحرك ووحدة اتصال.

## روابط مفيدة

- [Breadboard Tutorial (Wikipedia)](https://en.wikipedia.org/wiki/Breadboard)
- [How to Use a Breadboard (Adafruit)](https://learn.adafruit.com/breadboards-for-beginners)
- [Breadboard Basics Tutorial](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [Adafruit — Breadboards](https://www.adafruit.com/category/65)
