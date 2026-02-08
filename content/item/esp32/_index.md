---
title: "ESP32 DevKit — لوحة تطوير WiFi + Bluetooth"
weight: 11
description: "لوحة تطوير لشريحة ESP32 من Espressif، مناسبة لمشاريع IoT والاستشعار."
image: "images/esp32.jpg"
---

لوحة تطوير لشريحة ESP32 من Espressif، مناسبة لمشاريع IoT والاستشعار والتحكم اللاسلكي.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| SoC | ESP32 (Xtensa LX6 dual-core @ 240 MHz) |
| الذاكرة | 520 KB SRAM, 4 MB Flash (نموذجي للـ DevKit) |
| Wi‑Fi | 802.11 b/g/n |
| Bluetooth | Bluetooth Classic + BLE 4.2 |
| الجهد | 3.0 V – 3.6 V (دخل 5 V عبر USB مع منظم) |
| GPIO | 34× GPIO (18× ADC, 2× DAC, touch، إلخ) |
| الواجهات | I2C, SPI, UART, PWM |

## أمثلة الاستخدام

- برمجة عبر Arduino IDE: تثبيت "ESP32 by Espressif" وتشغيل مثال WiFi أو BLE.
- استخدام ESP-IDF لبناء تطبيق C مع استغلال كامل للميزات.
- توصيل مستشعر وإرسال البيانات إلى MQTT أو خادم ويب.

## روابط مفيدة

- [ESP32 Datasheet (Espressif)](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)
- [ESP32 DevKitC (Espressif)](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-devkitc.html)
- [Arduino-ESP32](https://github.com/espressif/arduino-esp32)
