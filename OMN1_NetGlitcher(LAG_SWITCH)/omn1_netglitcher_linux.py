#!/usr/bin/env python3

import os
import time
import subprocess
import threading
import keyboard

def banner():
    print(r"""
 ██████╗ ███╗   ███╗███╗   ██╗███╗   ██╗
██╔═══██╗████╗ ████║████╗  ██║████╗  ██║
██║   ██║██╔████╔██║██╔██╗ ██║██╔██╗ ██║
██║   ██║██║╚██╔╝██║██║╚██╗██║██║╚██╗██║
╚██████╔╝██║ ╚═╝ ██║██║ ╚████║██║ ╚████║
 ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝
        OMN1_NETGLITCHER v1.3

  Educational Network Disruption Simulator
   Created for safe local testing & audits.
      Use responsibly. Root access required.
""")

def run_cmd(cmd):
    print(f"[+] Executing: {cmd}")
    result = subprocess.run(cmd, shell=True, stderr=subprocess.PIPE)
    if result.stderr:
        print(result.stderr.decode())

def add_delay(interface, delay):
    run_cmd(f"tc qdisc add dev {interface} root netem delay {delay}ms")

def add_loss(interface, percent):
    run_cmd(f"tc qdisc add dev {interface} root netem loss {percent}%")

def clear_tc(interface):
    run_cmd(f"tc qdisc del dev {interface} root")

def block_port(port, duration):
    run_cmd(f"iptables -A OUTPUT -p udp --dport {port} -j DROP")
    print(f"[!] UDP port {port} blocked for {duration} seconds...")
    time.sleep(duration)
    run_cmd(f"iptables -D OUTPUT -p udp --dport {port} -j DROP")

def block_udp_all(duration):
    run_cmd("iptables -A OUTPUT -p udp -j DROP")
    run_cmd("iptables -A INPUT -p udp -j DROP")
    print(f"[!] ALL UDP traffic blocked for {duration} seconds...")
    time.sleep(duration)
    run_cmd("iptables -D OUTPUT -p udp -j DROP")
    run_cmd("iptables -D INPUT -p udp -j DROP")

def block_all(duration):
    run_cmd("iptables -A OUTPUT -j DROP")
    run_cmd("iptables -A INPUT -j DROP")
    print(f"[!] ALL INTERNET TRAFFIC (TCP + UDP) BLOCKED for {duration} seconds...")
    time.sleep(duration)
    run_cmd("iptables -D OUTPUT -j DROP")
    run_cmd("iptables -D INPUT -j DROP")

def get_interfaces():
    result = subprocess.run("ls /sys/class/net", shell=True, capture_output=True, text=True)
    interfaces = result.stdout.strip().split("\n")
    interfaces = [iface for iface in interfaces if iface != "lo" and not iface.startswith("veth")]
    return interfaces

def choose_interface():
    interfaces = get_interfaces()
    if not interfaces:
        print("[!] No active network interfaces found.")
        exit(1)

    print("\nDetected network interfaces:")
    for idx, iface in enumerate(interfaces, start=1):
        print(f"[{idx}] {iface}")

    while True:
        try:
            choice = int(input("Select an interface by number: "))
            if 1 <= choice <= len(interfaces):
                return interfaces[choice - 1]
            else:
                print("[!] Invalid selection. Try again.")
        except ValueError:
            print("[!] Please enter a valid number.")

def start_hotkey_listener():
    def listen():
        while True:
            keyboard.wait("u")
            print("\n[*] Hotkey U pressed — Blocking ALL UDP traffic for 5 seconds...")
            block_udp_all(5)
            print("[✔] UDP unblocked. Returning to menu...\n")
    listener = threading.Thread(target=listen, daemon=True)
    listener.start()

def main_menu():
    if os.geteuid() != 0:
        print("[!] This program must be run as root. Please use: sudo python3 omn1_netglitcher_linux.py")
        exit(1)

    banner()
    interface = choose_interface()
    start_hotkey_listener()

    while True:
        print("\n===== OMN1_NETGLITCHER - Main Menu =====")
        print(f"[✔] Selected interface: {interface}")
        print("[1] Add packet delay")
        print("[2] Simulate packet loss")
        print("[3] Lagswitch – block specific UDP port temporarily")
        print("[4] Clear all traffic control settings")
        print("[5] Block ALL UDP traffic temporarily")
        print("[6] Block ALL internet traffic (TCP + UDP) temporarily")
        print("[7] Exit")
        print("[U] 🔥 Hotkey: Press 'U' anytime to block ALL UDP for 5 seconds(Testing in games)")
        choice = input("Choose an option (1–7): ").strip()

        if choice == "1":
            delay = input("Enter delay in milliseconds (e.g., 300): ").strip()
            add_delay(interface, delay)
        elif choice == "2":
            loss = input("Enter packet loss percentage (e.g., 10): ").strip()
            add_loss(interface, loss)
        elif choice == "3":
            port = input("Enter UDP port number (e.g., 27015): ").strip()
            duration = input("Enter duration in seconds (e.g., 5): ").strip()
            block_port(int(port), int(duration))
        elif choice == "4":
            clear_tc(interface)
        elif choice == "5":
            duration = input("Enter duration in seconds to block ALL UDP: ").strip()
            block_udp_all(int(duration))
        elif choice == "6":
            duration = input("Enter duration in seconds to block ALL internet: ").strip()
            block_all(int(duration))
        elif choice == "7":
            print("[✔] Exiting... clearing traffic control rules.")
            clear_tc(interface)
            break
        else:
            print("[!] Invalid option. Please choose 1–7.")

if __name__ == "__main__":
    main_menu()
