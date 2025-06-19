OMN1_NETGLITCHER

Version: 1.3
Author: @mgledevStatus: Private Educational Tool

🎯 Overview

OMN1_NETGLITCHER is a professional, educational tool designed for local testing of network disruptions. It allows for temporary blocking or degradation of UDP and TCP traffic to simulate lags, packet loss, and latency issues.

⚠️ This is NOT a cheating tool. It is intended for ethical, offline testing environments (e.g. AI reaction tests, replay analysis, protocol debugging, or educational demonstrations). However, the tool has been successfully tested in online multiplayer games for analyzing network behavior under extreme conditions.

🕹️ In online games, the effect is similar to a "lag switch": the player temporarily loses connection (UDP is dropped), can freely move around the map (without being detected by the server), gather situational data (positions, angles), and upon reconnection, returns to the position they were in before the disconnection. This behavior is useful for understanding how netcode and server reconciliation work under packet loss or timeout scenarios.

🛠️ Features

✅ UDP port-specific blocking (lagswitch-style)

✅ Total UDP blackout (INPUT + OUTPUT)

✅ Full Internet cut (TCP + UDP)

✅ Packet delay injection (ms-based)

✅ Packet loss simulation (%-based)

✅ Real-time hotkey triggering (U for instant UDP lag)

✅ Works on any Linux with iptables, tc, and python

✅ Tested in online games (CS2, Valorant, etc.) for controlled simulations

✅ Windows version available (private) using WinDivert + Python wrapper

💻 Requirements

Linux (Kali, Arch, Garuda, etc.)

iptables and tc installed

sudo privileges

Python 3.9+

Python packages:

pip install keyboard

🚀 Usage

This repository does not include source code.
The tool is maintained privately by the author.

If you'd like to see how it works:

Clone the repo

Use the binary release or compiled .pyz / .pyc file (when provided)
 

❌ This repo does not contain source code

The source code for OMN1_NETGLITCHER is not public and will remain private for security, ethical and operational reasons.

A Windows version based on WinDivert + Python has been developed and is also private.

📄 License

All rights reserved. Do not redistribute binaries without permission.This project is intended for educational & research purposes only.

🤝 Contact

Want to collaborate or suggest features?

GitHub: github.com/mgledev

🔒 Disclosure

This tool is not affiliated with or endorsed by Valve, Faceit, or any gaming platform. It must not be used to gain competitive advantage or violate any terms of service.

