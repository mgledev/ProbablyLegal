# 🧪 ProbablyLegal – Educational Sandbox of Grey-Zone Ideas

**ProbablyLegal** is a personal lab of experimental, slightly questionable (but still legal) projects that explore the grey area between creativity, hardware control, and AI.  
Here you'll find tools that mix fun, curiosity, and machine intelligence — all designed for **research, prototyping, and educational use only**.

---

## 🎯 Currently Included

### ▸ `VisualTriggerAI/`

A real-time computer vision system that analyzes a streamed gameplay window using YOLOv9c and triggers an external device (e.g., Teensy via UART) when specific visual conditions are met.

> 🧠 Combines AI, object detection, serial communication, and human-like behavior simulation (e.g., random delay and probabilistic triggers).


🌐 OMN1_NetGlitcher/

    A controlled network glitch tool for testing game engines, latency behavior, and UDP resilience — all locally and legally.

OMN1_NetGlitcher is an educational lagswitch-style tool that simulates short bursts of packet loss or delay on Linux and Windows.

🧩 Built by mgledev for testing, research, and reverse-engineering purposes, it allows you to:

    Temporarily block UDP, TCP, or both, either manually or via keyboard shortcut (e.g., press U to lag for 5 seconds)

    Emulate network instability to analyze game engine behavior (rollback, interpolation, netcode handling)

    Run offline with bots or in controlled environments

    Test how far a player can move during a lag spike before sync catches up

🎯 Use cases include:

    Reverse-engineering movement prediction in FPS games

    Evaluating anti-lag mechanisms

    Simulating real-world packet drops in educational labs

    Teaching students about UDP/TCP reliability and recovery

⚠️ Legal & Ethical Use:

This tool is:

🧪 For educational sandbox testing
🚫 Not to be used in online matches or against other players
🛑 Not a cheat — it simulates client-side lag in isolated setups only

🔒 A Windows version also exists (WinDivert-based) but is private.

🛠️ Requires: iptables (Linux), or WinDivert (Windows)

---

## ⚠️ Legal & Ethical Use

All tools in this repository are:

- 🧪 Experimental
- 🎓 Educational
- 🔌 Built for hardware, AI, and automation research
- ❌ Not intended for online games, cheating, or commercial exploitation

You are fully responsible for how you use this code.  
If you're unsure whether you should run something from here, the answer is probably:

> **You probably shouldn't.** 😉


---

## 🔧 Getting Started

Each project is self-contained in its own folder with its own dependencies, usage instructions, and legal disclaimer.  


⚖️ License

This repository uses a custom MIT-style license with educational restrictions.
All tools are provided as-is, without any warranty.

    Use wisely. Build cool stuff. Stay Probably Legal.
