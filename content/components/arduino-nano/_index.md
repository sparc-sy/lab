---
title: "Arduino Nano — لوحة تحكم دقيقة"
weight: 15
description: "لوحة Arduino رسمية أو متوافقة صغيرة الحجم للتطوير السريع والمشاريع المدمجة."
image: "https://upload.wikimedia.org/wikipedia/commons/2/22/Arduino_Nano_front_zoom.jpg"
---

لوحة Arduino رسمية أو متوافقة صغيرة الحجم، مناسبة للتطوير السريع والمشاريع المدمجة.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| MCU | ATmega328P (AVR 8-bit @ 16 MHz) |
| Flash | 32 KB |
| SRAM | 2 KB |
| EEPROM | 1 KB |
| الجهد | 5 V (دخل 7–12 V موصى للاستقرار) |
| I/O | 14 digital (6 PWM), 8 analog input |
| الواجهات | UART (D0/D1), I2C (A4/A5), SPI (D10–D13) |

## أمثلة الاستخدام

- فتح Arduino IDE واختيار لوحة "Arduino Nano" وتحميل مثال Blink أو DigitalRead.
- توصيل مستشعر I2C (مثل BME280) وقراءته عبر مكتبة Wire.
- التحكم بمحرك أو LED عبر PWM على المنافذ 3, 5, 6, 9, 10, 11.

## روابط مفيدة

- [Official Product Page (Arduino Nano)](https://docs.arduino.cc/hardware/nano)
- [Datasheet (ATmega328P)](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf)
- [Official Examples (Built-in Arduino Examples)](https://docs.arduino.cc/built-in-examples/)
