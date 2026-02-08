---
title: "ESP32-CAM — موديول رؤية حاسوبية اقتصادي"
weight: 12
description: "موديول ESP32 مع كاميرا OV2640 مدمجة للمراقبة والبث والتصوير."
image: "images/cam.jpg"
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

- [ESP32-CAM Module Datasheet](https://www.handsontec.com/dataspecs/module/ESP32-CAM.pdf)
- [OV2640 Camera Sensor Datasheet](https://github.com/raphaelbs/esp32-cam-ai-thinker/blob/master/assets/OV2640_Datasheet.pdf)
- [ESP32-CAM (AI-Thinker) documentation](https://github.com/espressif/esp32-camera)
- [Arduino ESP32 Camera examples](https://github.com/espressif/esp32-camera/tree/master/examples)
