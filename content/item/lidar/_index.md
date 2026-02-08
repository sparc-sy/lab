---
title: "EAI YDLIDAR X2L — ليدار ثنائي الأبعاد"
weight: 4
description: "ليدار ليزري 2D من EAI مع دعم ROS."
image: "images/lidar.jpg"
---

ليدار ليزري 2D من EAI مناسب للروبوتات التعليمية والبحثية، مع دعم ROS وبرامج مسح على Windows/Linux.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| الجهد | 5 V (USB) |
| المدى | 0.12 m – 12 m |
| الدقة | ±3 cm |
| زاوية المسح | 360° |
| التردد | 5–12 Hz (حسب الإعداد) |
| الطول الموجي | 785 nm |
| الواجهة | USB (virtual serial) |

## أمثلة الاستخدام

- تشغيل **YDLIDAR SDK** على Windows/Linux وجمع نقاط المسح.
- دمج مع **ROS** عبر حزمة `ydlidar_ros_driver` لـ SLAM (مثل gmapping).
- عرض النقاط في برنامج مثل RViz أو تطبيق مخصص.

## روابط مفيدة

- [YDLIDAR X2 product page](https://www.ydlidar.com/product/ydlidar-x2)
- [YDLIDAR X2 Datasheet (PDF)](https://robu.in/wp-content/uploads/2021/01/YDLIDAR-X2-Data-Sheet-V1.2240124.pdf)
- [YDLIDAR X2 User Manual](https://www.ydlidar.com/Public/upload/files/2024-02-01/YDLIDAR%20X2%20Lidar%20User%20Manual%20V1.3(240124).pdf)
- [YDLIDAR SDK (GitHub)](https://github.com/YDLIDAR/YDLidar-SDK)
- [YDLIDAR ROS](https://github.com/YDLIDAR/ydlidar_ros)
