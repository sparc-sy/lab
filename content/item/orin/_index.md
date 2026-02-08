---
title: "NVIDIA Jetson Orin Nano (8GB) — منصة حوسبة حافة AI"
weight: 7
description: "منصة تطوير وتشغيل تطبيقات الذكاء الاصطناعي على الحافة من NVIDIA."
image: "images/orin.png"
---

منصة تطوير وتشغيل تطبيقات الذكاء الاصطناعي على الحافة من NVIDIA (Jetson Orin Nano 8 GB)، مناسبة للمشاريع التعليمية والصناعية والروبوتات.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| SoC | Jetson Orin Nano (6-core Arm Cortex-A78AE، 1024 CUDA core، 32 Tensor core) |
| الذاكرة | 8 GB 128-bit LPDDR5 (68 GB/s) |
| أداء AI | حتى 40 TOPS INT8 (Sparse)، 20 TOPS (Dense) |
| جهد الدخل | 5 V–19 V DC |
| الواجهات | USB 3.2، GbE، GPIO، M.2 (Key M، Key E)، HDMI، MIPI CSI (كاميرات) |
| JetPack | Ubuntu 20.04، CUDA، cuDNN، TensorRT |

## أمثلة الاستخدام

- تثبيت JetPack وتشغيل حزمة **Hello AI World** (تصنيف صور، كشف كائنات) ثم ربط كاميرا أو عدة كاميرات.
- استخدام **DeepStream** لتحليل فيديو متعدد القنوات (مراقبة، عدّ، تحذير).
- تشغيل نماذج PyTorch/TensorFlow محولة إلى TensorRT لتسريع الاستنتاج على الروبوت أو البوابة الذكية.

## روابط مفيدة

- [Jetson Orin Nano Developer Kit Getting Started](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit)
- [Jetson Orin Nano User Guide](https://developer.nvidia.com/embedded/learn/jetson-orin-nano-devkit-user-guide/index.html)
- [Jetson Orin Nano Datasheet (PDF)](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5380/Jetson_Orin_Nano_Series_DS-11105-001_v1.1.pdf)
- [Jetson Orin Nano Carrier Board Specification](https://developer.download.nvidia.com/assets/embedded/secure/jetson/orin_nano/docs/Jetson-Orin-Nano-DevKit-Carrier-Board-Specification_SP-11324-001_v1.3.pdf)
- [JetPack SDK](https://developer.nvidia.com/embedded/jetpack)
- [Jetson Zoo (نماذج جاهزة)](https://elinux.org/Jetson_Zoo)
