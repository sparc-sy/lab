---
title: "GY-BNO080 / BNO085 — وحدة IMU 9DOF AHRS عالية الدقة"
weight: 3
description: "وحدة استشعار حركة من CEVA مع معالج داخلي لحساب الاتجاه (AHRS)."
image: "images/imu.jpg"
---

وحدة استشعار حركة 9DOF من CEVA (BNO085/BNO08x) مع معالج داخلي لحساب الاتجاه (AHRS) وتوفير كواتيرنيون ويولر وتسارع خطي. مناسبة لتطبيقات AR/VR والروبوتات والتحكم بالاتجاه.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| الجهد | 3.0 V – 3.6 V (VDD)، 1.71–3.6 V (VDDIO) |
| الاستهلاك | ~4.5 mA (نمط استشعار كامل) |
| الواجهات | I2C (حتى 400 kHz)، SPI، UART؛ عنوان I2C افتراضي 0x4A |
| المحاور | 3-axis accelerometer، gyroscope، magnetometer |
| المخرجات | Quaternion، Euler، linear acceleration؛ كشف نقر وخطى |
| معدل التحديث | حتى 400 Hz (IMU)، حتى 100 Hz (مغناطيس) |

## أمثلة الاستخدام

- استخدام مكتبة **Adafruit_BNO08x** لأردوينو أو CircuitPython لقراءة الكواتيرنيون واليولر واستقرار الاتجاه.
- على Raspberry Pi: استخدام I2C أو SPI مع مكتبات Python لربط الاتجاه بذراع روبوتي أو مركبة.
- دمج مع Unity أو تطبيق AR لقراءة الاتجاه في الوقت الفعلي؛ أو استخدام كشف النقر/الخطى لواجهات تفاعلية.

## روابط مفيدة

- [داتاشيت BNO085 (CEVA)](https://www.ceva-dsp.com/app-notes/)
- [Adafruit BNO08x](https://www.adafruit.com/product/4754)
- [Adafruit BNO08x Library](https://github.com/adafruit/Adafruit_BNO08x)
