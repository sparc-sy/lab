---
title: "ESP32-CAM — موديول رؤية حاسوبية اقتصادي"
weight: 12
description: "موديول ESP32 مع كاميرا OV2640 مدمجة للمراقبة والبث والتصوير."
image: "https://randomnerdtutorials.com/wp-content/uploads/2019/03/esp32-cam-ai-thinker-board-pinout-and-gpios-usage.jpg"
---

موديول ESP32 مع كاميرا OV2640 مدمجة، مناسب للمراقبة والبث والتصوير في مشاريع IoT.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| SoC | ESP32 (dual-core, 240 MHz) |
| الكاميرا | OV2640 (2 MP, UXGA 1600×1200, JPEG) |
| Flash | 4 MB (نموذجي) |
| الجهد | 5 V (مهم: تيار كافٍ ~500 mA) |
| الواجهة | Wi‑Fi، UART (للتوصيل والبرمجة)، GPIO محدود |

## أمثلة الاستخدام

- رفع مثال **CameraWebServer** من Arduino ESP32 وحفظه على اللوحة، ثم الدخول عبر المتصفح لعرض الفيديو والتحكم.
- التقاط صورة وإرسالها عبر HTTP أو MQTT إلى خادم.
- استخدام مكتبات التعرف على الوجوه (مثل ESP32 face recognition) إن توفرت للنسخة المستخدمة.

## روابط مفيدة

- [ESP32-CAM (AI-Thinker) documentation](https://github.com/espressif/esp32-camera)
- [ESP32 Camera driver](https://github.com/espressif/esp32-camera)
- [Arduino ESP32 Camera examples](https://github.com/espressif/arduino-esp32/tree/master/libraries/ESP32/examples/camera)
