---
title: "Sipeed Lichee Tang Nano 4K — لوحة FPGA GoAI مع كاميرا HDMI"
weight: 2
description: "لوحة تطوير FPGA من Sipeed/Gowin مع دعم GoAI وكاميرا HDMI."
image: "images/fpga.jpg"
---

لوحة تطوير FPGA من Sipeed/Gowin صغيرة الحجم، مع معالج ARM Cortex-M3 مدمج (80 MHz)، دعم كاميرا DVP وخرج HDMI، مناسبة للتعلم ومشاريع معالجة الصور والذكاء الاصطناعي على الحافة.

## المواصفات التفصيلية (من الداتاشيت)

| المواصفة | القيمة |
|----------|--------|
| FPGA | Gowin GW1NSR-LV4C (4608 LUT4، 3456 FF، 180 Kbit B-SRAM) |
| ذاكرة | 64 MB HyperRAM، 32 Mbit NOR Flash |
| معالج | ARM Cortex-M3 (80 MHz) مدمج |
| واجهات | HDMI (خارج)، DVP كاميرا (مثلاً OV2640)، USB Type-C (طاقة + JTAG)، 38 GPIO |
| جهد التشغيل | 5 V (عبر USB Type-C) |
| بيئة التطوير | Gowin EDA (VHDL/Verilog)، OpenFPGA |

## أمثلة الاستخدام

- تشغيل كاميرا DVP (مثل OV2640) أو إدخال HDMI وعرض الصورة عبر FPGA إلى شاشة.
- بناء مشروع GoAI لتصنيف الصور على اللوحة.
- تصميم دوائر رقمية (عدادات، UART، عرض على شاشة) أو خط معالجة صور بسيط (عتبة، تتبع لون).

## روابط مفيدة

- [Sipeed Wiki — Tang Nano 4K](https://wiki.sipeed.com/hardware/en/tang/Tang-Nano-4K/Nano-4K.html)
- [Tang Nano 4K Datasheet (PDF)](https://akizukidenshi.com/goodsaffix/Tang%20nano%204K.pdf)
- [Gowin GW1NSR FPGA Information](https://www.gowinsemi.com/en/support/devkits_detail/39/)
- [Gowin EDA](https://www.gowinsemi.com/)
- [مستودعات Sipeed (GitHub)](https://github.com/sipeed)
