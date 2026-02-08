---
title: "EAI YDLIDAR X2L — ليدار ثنائي الأبعاد"
weight: 4
description: "ليدار ليزري 2D من EAI مع دعم ROS."
image: "images/lidar.jpg"
---

ليدار ليزري 2D من EAI (YDLIDAR X2/X2L) يعتمد التثليث، مناسب للروبوتات التعليمية والبحثية، مع دعم ROS وبرامج مسح على Windows/Linux.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| الجهد | 5 V (USB) |
| المدى | 0.12 m – 8 m (نموذجي داخلي، حتى 12 m في ظروف مناسبة) |
| الدقة | ±2 cm (≤1 m)، ±3.5% (>1 m) |
| زاوية المسح | 360° |
| تردد المسح | 5–8 Hz (قابل للضبط؛ موصى 6 Hz) |
| الطول الموجي | 785 nm (Class I) |
| الواجهة | USB (virtual serial) |

## أمثلة الاستخدام

- تشغيل **YDLIDAR SDK** على Windows/Linux لجمع نقاط المسح وعرضها في تطبيق مخصص أو أداة المورد.
- دمج مع **ROS** عبر حزمة `ydlidar_ros_driver` لـ SLAM (gmapping، cartographer) أو تجنب عوائق لروبوت متحرك.
- بناء خريطة ثنائية الأبعاد لغرفة أو ممر للتنقل الآلي أو المراقبة.

## روابط مفيدة

- [YDLIDAR X2 product page](https://www.ydlidar.com/product/ydlidar-x2)
- [YDLIDAR X2 Datasheet (PDF)](https://robu.in/wp-content/uploads/2021/01/YDLIDAR-X2-Data-Sheet-V1.2240124.pdf)
- [YDLIDAR X2 User Manual](https://www.ydlidar.com/Public/upload/files/2024-02-01/YDLIDAR%20X2%20Lidar%20User%20Manual%20V1.3(240124).pdf)
- [YDLIDAR SDK (GitHub)](https://github.com/YDLIDAR/YDLidar-SDK)
- [YDLIDAR ROS](https://github.com/YDLIDAR/ydlidar_ros)
