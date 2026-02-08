---
title: "Hailo-8L — AI Kit لراسبيري باي"
weight: 10
description: "وحدة NPU من Hailo لتسريع استنتاج نماذج الذكاء الاصطناعي على Raspberry Pi."
image: "images/hailo.png"
---

وحدة NPU من Hailo مصممة للعمل مع Raspberry Pi لتسريع استنتاج نماذج الذكاء الاصطناعي.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| الشريحة | Hailo-8L |
| الأداء | 13 TOPS (INT8) |
| الاستهلاك | منخفض (يعمل من منفذ الراسبيري) |
| الواجهة | M.2 2242 أو USB 3 (حسب المنتج) |
| النماذج | YOLO، تصنيف صور، تقسيم، إلخ (عبر Hailo SDK) |

## أمثلة الاستخدام

- تثبيت Hailo SDK على Raspberry Pi وتشغيل أمثلة كشف الكائنات.
- تحويل نموذج مدرب (ONNX/TensorFlow) إلى تنسيق Hailo وتشغيله على الكيت.
- دمج الكاميرا مع خط أنابيب استنتاج Hailo لعرض النتائج في الوقت الفعلي.

## روابط مفيدة

- [Hailo-8 Product](https://hailo.ai/products/ai-accelerators/hailo-8/)
- [Hailo-8L Datasheet (PDF)](https://hailo.ai/files/hailo-8l-industrial-datasheet)
- [Hailo-8L Product Brief](https://hailo.ai/wp-content/uploads/2023/12/hailo8l_product_brief_1.2.pdf)
- [Hailo Developer Zone](https://hailo.ai/developer-resources/)
- [Hailo SDK / Documentation](https://hailo.ai/developer-resources/software-downloads/)
- [Hailo Python Examples](https://github.com/hailo-ai/hailo-rpi5-examples)
