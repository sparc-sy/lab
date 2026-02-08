---
title: "Hailo-8L — AI Kit لراسبيري باي"
weight: 10
description: "وحدة NPU من Hailo لتسريع استنتاج نماذج الذكاء الاصطناعي على Raspberry Pi."
image: "images/hailo.png"
---

وحدة NPU من Hailo (Hailo-8L) مصممة للعمل مع Raspberry Pi لتسريع استنتاج نماذج الذكاء الاصطناعي دون الحاجة لذكرى خارجية.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| الشريحة | Hailo-8L |
| الأداء | 13 TOPS (INT8)، متوافق برمجياً مع Hailo-8 |
| الاستهلاك | ~1.5 W typ. (يعمل من منفذ الراسبيري) |
| الواجهة | M.2 2242/2260/2280 (Key B+M) أو Key A+E حسب المنتج |
| النماذج | YOLO، تصنيف صور، تقسيم (عبر Hailo SDK؛ TensorFlow، PyTorch، ONNX) |

## أمثلة الاستخدام

- تثبيت Hailo SDK على Raspberry Pi وتشغيل أمثلة كشف الكائنات (YOLO) مع كاميرا في الوقت الفعلي.
- تحويل نموذج مدرب (ONNX/TensorFlow) إلى تنسيق Hailo وتشغيله على الكيت لاستدلال محلي منخفض الزمن.
- دمج الكاميرا مع خط أنابيب استنتاج متعدد القنوات أو متعدد النماذج لعرض النتائج على شاشة أو إرسالها عبر الشبكة.

## روابط مفيدة

- [Hailo-8 Product](https://hailo.ai/products/ai-accelerators/hailo-8/)
- [Hailo-8L Datasheet (PDF)](https://hailo.ai/files/hailo-8l-industrial-datasheet)
- [Hailo-8L Product Brief](https://hailo.ai/wp-content/uploads/2023/12/hailo8l_product_brief_1.2.pdf)
- [Hailo Developer Zone](https://hailo.ai/developer-resources/)
- [Hailo SDK / Documentation](https://hailo.ai/developer-resources/software-downloads/)
- [Hailo Python Examples](https://github.com/hailo-ai/hailo-rpi5-examples)
