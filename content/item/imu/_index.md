---
title: "GY-BNO080 / BNO085 — وحدة IMU 9DOF AHRS عالية الدقة"
weight: 3
description: "وحدة استشعار حركة من CEVA مع معالج داخلي لحساب الاتجاه (AHRS)."
image: "images/imu.jpg"
---

وحدة استشعار حركة من CEVA (Hillcrest Labs) تحتوي على معالج داخلي لحساب الاتجاه (AHRS) وتوفير كواتيرنيون ويولر. مناسبة لتطبيقات AR/VR والروبوتات.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| الجهد | 3.0 V – 3.6 V (VDD), 1.71–3.6 V (VDDIO) |
| الاستهلاك | ~4.5 mA (نمط استشعار كامل) |
| الواجهات | I2C (حتى 400 kHz), SPI (حتى 3 MHz), UART |
| المحاور | 3-axis accelerometer, gyroscope, magnetometer |
| المخرجات | Quaternion, Euler, linear acceleration, etc. |
| معدل التحديث | قابل للضبط (حتى 400 Hz) |

## أمثلة الاستخدام

- استخدام مكتبة **Adafruit_BNO08x** لأردوينو أو CircuitPython لقراءة الكواتيرنيون واليولر.
- على Raspberry Pi: استخدام I2C أو SPI مع مكتبات Python المناسبة.
- دمج مع Unity أو تطبيق AR لقراءة الاتجاه في الوقت الفعلي.

## روابط مفيدة

- [داتاشيت BNO085 (CEVA)](https://www.ceva-dsp.com/app-notes/)
- [Adafruit BNO08x](https://www.adafruit.com/product/4754)
- [Adafruit BNO08x Library](https://github.com/adafruit/Adafruit_BNO08x)
