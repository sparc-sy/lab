---
title: "AI Workstation — محطة عمل ذكاء اصطناعي"
weight: 19
description: "محطة عمل عالية الأداء لدعم الاستدلال المحلي، التدريب/الضبط الدقيق، والرؤية الحاسوبية في مختبرات الذكاء الاصطناعي."
image: "images/workstation.jpg"
---

منصة مكتبية موحدة لمختبرات الذكاء الاصطناعي، تجمع بين قدرة حوسبة مرتفعة ومرونة توسعة لتشغيل أعباء العمل البحثية والتعليمية محليًا.

## Workstation Subcomponents

| Subcomponent | Exact Model |
|--------------|-------------|
| CPU | Intel Core Ultra 9 285K |
| GPU | NVIDIA RTX 5090 |
| RAM | DDR5-6400 128 GB |
| Storage | NVMe M.2 2 TB |
| PSU | 1000 W 80+ Platinum PSU |

## AI Lab Use Cases

- **Local model inference**: تشغيل نماذج LLM/VLM محليًا لأغراض الخصوصية، خفض زمن الاستجابة، والعمل دون اعتماد دائم على السحابة.
- **Training & fine-tuning workflows**: تدريب تجارب صغيرة إلى متوسطة، وضبط دقيق لنماذج مفتوحة المصدر باستخدام PyTorch/TensorFlow وتسريع GPU.
- **Computer vision pipelines**: تطوير خطوط معالجة فيديو/صور (تصنيف، كشف كائنات، تتبع) واختبار الأداء قبل النشر على أنظمة الحافة (Jetson، ESP32).
- **Robotics & edge development support**: بناء واختبار برمجيات ROS2، المحاكاة، وتجهيز النماذج للنشر على لوحات طرفية.

## Configuration/Upgrade Paths

- **Alternate GPU tier**: اختيار فئة GPU أقل عندما يكون التركيز على التطوير التعليمي أو الاستدلال الخفيف، أو فئة أعلى عند الحاجة لتدريب أكبر/نماذج أثقل.
- **Memory expansion**: زيادة الذاكرة (مثل 192GB أو 256GB حسب اللوحة) مناسبة للأعباء متعددة الحاويات، مجموعات بيانات أكبر، أو تشغيل نماذج متعددة بالتوازي.
- **Storage scaling**: إضافة أقراص NVMe/SATA إضافية عند الحاجة إلى أرشفة datasets، checkpoints، وسجلات التجارب طويلة الأمد.
- **Power/cooling enhancements**: ترقية التبريد الهوائي/السائل أو مزود الطاقة عند زيادة الحمل المستمر أو عند إضافة بطاقات/أقراص إضافية.

## Operational Guidance for AI Labs

- **Power & thermals**: يُنصح بدائرة كهربائية مستقرة، UPS للأعمال الحرجة، وتدفق هواء جيد مع مراقبة درجات الحرارة تحت حمل طويل.
- **Reliability practices**: استخدام خطط نسخ احتياطي منتظمة، مراقبة SMART للأقراص، وتثبيت إصدارات التعريفات/الحزم لتقليل أعطال البيئة.
- **Expected workloads**: مناسبة للاستدلال الكثيف، الضبط الدقيق، المعالجة الدُفعية (batch processing)، والتجارب المتكررة في بيئات بحثية.
- **Software stack assumptions**: Linux (Ubuntu LTS)، NVIDIA Driver + CUDA/cuDNN، Docker/Compose، Python ML stack (PyTorch, TensorFlow, Jupyter, MLflow) حسب سياسة المختبر.

## روابط مفيدة

- [Intel Core Ultra 9 285K Specifications](https://www.intel.com/content/www/us/en/products/sku/239504/intel-core-ultra-9-processor-285k-36m-cache-up-to-5-70-ghz/specifications.html)
- [NVIDIA RTX 5090 Specifications](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/)
- [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit)
- [PyTorch Installation Guide](https://pytorch.org/get-started/locally/)
- [TensorFlow Installation Guide](https://www.tensorflow.org/install)
