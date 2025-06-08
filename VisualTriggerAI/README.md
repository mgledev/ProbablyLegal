# 🎯 VisualTriggerAI

**VisualTriggerAI** is an experimental, research-driven system that uses real-time object detection to analyze a live video stream and trigger external hardware (e.g., via UART) based on visual criteria.

It’s like having a robot friend who watches your screen and sometimes *gets excited*.  
Built strictly for **educational and research purposes**.

---

## 🚀 Features

- 🧠 YOLOv9c model-based visual detection (because YOLO, right?)
- ⚡ GPU acceleration via CUDA (optional, but makes it spicy)
- 🎲 Randomized trigger chance (~15%) — because even robots need unpredictability
- ⏱️ Human-ish reaction delays (85–135ms)
- 🔌 UART signal output (connects to friendly hardware)
- 🖼️ Real-time live overlay and preview window

---
## 🧠 System Architecture (2-PC + Teensy)

🎮 PC1 (CLEAN PC WITH GAME)(no AI) 📡  ➡️  🧠 PC2 (AI): VisualTriggerAI
USB ⬅️ Teensy ← UART signal ⬅️ YOLOv9c visual detection


- Game runs on PC1 (clean)
- Screen is streamed to PC2 (via Moonlight etc.)
- PC2 analyzes frames, decides whether to activate
- UART signal is sent to Teensy, which simulates mouse input on PC1

---

🛡️ HID Emulation (Optional)

To increase stealth (and because your USB stick dreams of being a mouse), you might consider configuring your device to act like a totally ordinary, totally boring USB HID peripheral. You know, the kind that nobody ever questions.
🧪 What You Could (Allegedly) Do:

    Pretend to be something... rodent-like 🐭

    Use vendor/product IDs that look familiar

    Pick a manufacturer name that feels corporate

    Generate a serial number that's random enough to be ignored

We’re not saying you should pretend to be a [REDACTED] mouse…
But if your device wants to blend in at a Windows party — well, who are we to judge?

    💡 All of this is, of course, purely optional and 100% educational.
    Use responsibly. Obey the law. Respect USB mice.

---

## ⚙️ Requirements

- Python 3.9+
- `ultralytics`, `opencv-python`, `torch`, `pyserial`, `keyboard`, `mss`, etc.
- UART-capable microcontroller (e.g., Teensy)
- Game video stream (e.g., Moonlight)

```bash
pip install -r requirements.txt


📚 Disclaimer

This project is intended for educational use only.
Do not deploy, distribute, or use in any setting that would violate terms of service, user agreements, or your local laws.

We do not condone or encourage misuse.
But we do encourage curiosity, creativity, and a sense of humor. 😎

🤖 Final Thoughts

VisualTriggerAI is here to make your computer think with its eyes.
What it does with that vision... is entirely up to your imagination (and your ethics).

> ⚠️ This software is released under the MIT License.  
> Please use it responsibly, ethically, and in compliance with all applicable laws.  
> This is an educational project — not a tool for competitive advantage, mischief, or domination of online rodents.

