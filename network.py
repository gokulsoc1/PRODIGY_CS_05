import socket
import struct
import datetime
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

# ---------------- Protocol Resolver ----------------
def protocol_name(proto):
    if proto == 1:
        return "ICMP"
    elif proto == 6:
        return "TCP"
    elif proto == 17:
        return "UDP"
    else:
        return "OTHER"

# ---------------- Packet Sniffer ----------------
def sniff_packets():
    global running
    try:
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        host_ip = socket.gethostbyname(socket.gethostname())
        sniffer.bind((host_ip, 0))
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        while running:
            packet, _ = sniffer.recvfrom(65535)

            ip_header = packet[:20]
            iph = struct.unpack("!BBHHHBBH4s4s", ip_header)

            src_ip = socket.inet_ntoa(iph[8])
            dst_ip = socket.inet_ntoa(iph[9])
            proto = iph[6]
            ttl = iph[5]

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            packet_data = (
                f"[{timestamp}]\n"
                f"Source IP      : {src_ip}\n"
                f"Destination IP : {dst_ip}\n"
                f"Protocol       : {protocol_name(proto)}\n"
                f"TTL            : {ttl}\n"
                f"{'-'*60}\n"
            )

            text_area.insert(tk.END, packet_data)
            text_area.yview(tk.END)

        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

    except PermissionError:
        messagebox.showerror("Permission Error", "Run VS Code as Administrator")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------- Control Functions ----------------
def start_capture():
    global running
    if not running:
        running = True
        threading.Thread(target=sniff_packets, daemon=True).start()
        start_btn.config(state=tk.DISABLED)
        stop_btn.config(state=tk.NORMAL)

def stop_capture():
    global running
    running = False
    start_btn.config(state=tk.NORMAL)
    stop_btn.config(state=tk.DISABLED)

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Network Packet Analyzer (Ethical Use)")
root.geometry("850x520")

title = tk.Label(
    root,
    text="Network Packet Analyzer\n(Live Packets | GUI | Built-in)",
    font=("Arial", 14, "bold")
)
title.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

start_btn = tk.Button(btn_frame, text="Start Capture", width=15, command=start_capture)
start_btn.pack(side=tk.LEFT, padx=10)

stop_btn = tk.Button(
    btn_frame,
    text="Stop Capture",
    width=15,
    command=stop_capture,
    state=tk.DISABLED
)
stop_btn.pack(side=tk.LEFT, padx=10)

text_area = ScrolledText(
    root,
    width=100,
    height=22,
    font=("Consolas", 10)
)
text_area.pack(padx=10, pady=10)

footer = tk.Label(
    root,
    text="Educational & Ethical Network Analysis Only",
    font=("Arial", 9)
)
footer.pack(pady=5)

running = False
root.mainloop()