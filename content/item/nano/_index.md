---
title: "Arduino Nano — لوحة تحكم دقيقة"
weight: 15
description: "لوحة Arduino رسمية أو متوافقة صغيرة الحجم للتطوير السريع والمشاريع المدمجة."
image: "images/nano.jpg"
---

لوحة Arduino رسمية أو متوافقة صغيرة الحجم (حوالي 18×45 mm)، مناسبة للتطوير السريع والمشاريع المدمجة والتركيب على breadboard.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| MCU | ATmega328P (AVR 8-bit @ 16 MHz) |
| Flash | 32 KB |
| SRAM | 2 KB |
| EEPROM | 1 KB |
| الجهد | 5 V منطق؛ دخل 7–12 V (Vin) موصى للاستقرار |
| I/O | 14 digital (6 PWM)، 8 analog input |
| الواجهات | UART (D0/D1)، I2C (A4/A5)، SPI (D10–D13) |

## أمثلة الاستخدام

- فتح Arduino IDE واختيار لوحة "Arduino Nano" وتحميل مثال Blink أو DigitalRead ثم ربط مستشعر أو محرك.
- توصيل مستشعر I2C (BME280، MPU6050) وقراءته عبر مكتبة Wire؛ أو SPI لشاشة أو ذاكرة.
- التحكم بمحرك أو LED عبر PWM على المنافذ 3، 5، 6، 9، 10، 11؛ مناسب لنماذج أولية صغيرة أو مشاريع تعليمية مدمجة.

## روابط مفيدة

- [Arduino Nano (الموقع الرسمي)](https://docs.arduino.cc/hardware/nano)
- [ATmega328P Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf)
- [Getting Started with Arduino Nano](https://docs.arduino.cc/tutorials/nano/nano-getting-started/)
- [Arduino Example Code Repository](https://github.com/arduino/arduino-examples)
- [Arduino Reference](https://www.arduino.cc/reference/en/)
