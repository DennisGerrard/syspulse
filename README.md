# SysPulse 🚀

[![Language: Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform: Linux](https://img.shields.io/badge/Platform-Linux-lightgrey.svg)](https://www.kernel.org/)

**SysPulse** is a lightweight, high-speed CLI system diagnostic tool and network geolocation extractor built for Linux environments. It aggregates core local hardware and kernel metrics alongside remote IP geolocation data, presenting everything in a clean, terminal-native dashboard.

---

## ⚡ Features

* 💻 **Local System Diagnostics:** Directly extracts Linux distribution name, kernel release, system architecture, active network interface MAC address, and native machine ID without heavy subprocess calls.
* 🌐 **Public Geolocation Lookup:** Retrieves public IP metadata, ISP details, organization info, and geographical coordinates.
* 🎨 **Styled Terminal Output:** Utilizes `rich` tables and panels for clear, color-coded visual presentation.
* 📄 **JSON & Export Modes:** Supports raw JSON output for stdout piping or direct file exporting for logging and reporting.
* 📦 **Zero Global Pollution:** Ships with a single-line automated installer that handles isolated virtual environments and global symlinking.
