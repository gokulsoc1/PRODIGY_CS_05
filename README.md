# PRODIGY_CS_02
#  Network Packet Analyzer (Python GUI)

The **Network Packet Analyzer** is a Python-based desktop application that captures and analyzes network packets in real time. It provides a graphical user interface (GUI) built with **Tkinter** that allows users to monitor incoming and outgoing packets on their system.

This tool demonstrates how **raw sockets, packet parsing, and GUI development** can be combined to create a simple network monitoring application. It is intended for **educational and ethical cybersecurity learning purposes**.

---

#  Project Overview

Network packet analysis is an important concept in **network security, cybersecurity, and system administration**. By examining packets traveling across a network, developers and security professionals can understand how communication occurs between devices.

This project captures packets from the network interface and extracts important information such as:

- Source IP address  
- Destination IP address  
- Protocol type  
- Time-to-Live (TTL) value  
- Timestamp of packet capture  

All captured data is displayed live in a scrollable GUI window.

---

#  Features

- 📡 Live network packet capturing
- 🖥️ Simple graphical user interface
- 📊 Displays packet information in real time
- 🔍 Identifies protocol types (TCP, UDP, ICMP)
- 🕒 Shows packet timestamp
- 🌍 Displays source and destination IP addresses
- ⚡ Start and stop capture controls
- 🧵 Uses multithreading for smooth GUI performance
- 📜 Scrollable packet log display
- 🎓 Designed for **educational cybersecurity practice**

---

#  How Packet Sniffing Works

Network communication happens through **packets**, which are small units of data transmitted between devices.

This program uses **raw sockets** to capture packets directly from the network layer.

The process includes:

1. Creating a raw socket
2. Listening for incoming packets
3. Extracting the IP header
4. Parsing packet information
5. Displaying packet details in the GUI

---

#  Packet Information Extracted

Each captured packet displays the following information:

| Field | Description |
|------|-------------|
| Timestamp | Time when packet was captured |
| Source IP | Address of sender |
| Destination IP | Address of receiver |
| Protocol | Communication protocol used |
| TTL | Time-To-Live value |


---

# Supported Protocols

The analyzer detects common network protocols:

| Protocol Number | Protocol Name |
|----------------|---------------|
| 1 | ICMP |
| 6 | TCP |
| 17 | UDP |
| Others | OTHER |

These protocols represent different types of network communication.

---

# Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python | Core programming language |
| Tkinter | GUI interface |
| Socket Library | Network packet capture |
| Struct | Binary packet parsing |
| Threading | Background packet capture |
| Datetime | Timestamp generation |

---

---

# ⚙️ Requirements

To run this project you need:

- Python **3.x**
- Administrative privileges (required for raw sockets)


#  Required Python Libraries

Install the required libraries using pip:

```bash
pip install socket struct tkinter datetime 


---


