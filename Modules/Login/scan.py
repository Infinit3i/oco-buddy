import os
import subprocess
import sys
from datetime import datetime
import threading

# Global list to store background tasks
BACKGROUND_TASK = []

def check_nmap():
    try:
        subprocess.run(["nmap", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except FileNotFoundError:
        print("Nmap is not installed on this system.")
        install_nmap()

def install_nmap():
    try:
        if sys.platform.startswith("linux"):
            print("Attempting to install nmap on Linux...")
            subprocess.run(["sudo", "apt-get", "update"], check=True)
            subprocess.run(["sudo", "apt-get", "install", "-y", "nmap"], check=True)
            print("Nmap installed successfully!")
        elif sys.platform.startswith("win"):
            print("Please download and install Nmap manually from: https://nmap.org/download.html")
        else:
            print("Unsupported operating system. Please install Nmap manually.")
            sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error installing Nmap: {e}")
        sys.exit(1)

def scan_ports(target_ip, box_name):
    check_nmap()  # Ensure nmap is installed
    print(f"Scanning {target_ip} for open ports (Fast scan)...")
    try:
        os.makedirs(box_name, exist_ok=True)  # Create folder for box results

        # Run Nmap to quickly scan the top 1000 ports
        result = subprocess.run(
            ["nmap", "-F", target_ip],
            text=True,
            capture_output=True,
            check=True,
        )
        output = result.stdout
        open_ports = []
        for line in output.splitlines():
            if "/tcp" in line and "open" in line:
                port = line.split("/")[0]
                open_ports.append(port)
        print(f"Open Ports: {', '.join(open_ports)}")
        
        # Add detailed Nmap scan to background tasks
        BACKGROUND_TASK.append(f"Nmap -sVC {target_ip}")
        threading.Thread(target=detailed_scan, args=(target_ip, box_name), daemon=True).start()

        # Check for web ports and start Gobuster if necessary
        if "80" in open_ports or "443" in open_ports:
            BACKGROUND_TASK.append(f"Gobuster http://{target_ip}")
            threading.Thread(target=run_gobuster, args=(target_ip,), daemon=True).start()

        return open_ports
    except subprocess.CalledProcessError as e:
        print(f"Error running Nmap: {e.stderr}")
        sys.exit(1)

def detailed_scan(target_ip, box_name):
    current_date = datetime.now().strftime("%Y-%m-%d")
    output_file_base = os.path.join(box_name, f"{target_ip}-{current_date}")
    try:
        subprocess.run(
            ["nmap", "-sVC", target_ip, "-oA", output_file_base], check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running detailed Nmap scan: {e}")

def run_gobuster(target_ip):
    """
    Run Gobuster for ports 80 or 443.
    :param target_ip: The target IP address.
    """
    try:
        subprocess.run(
            ["gobuster", "dir", "-u", f"http://{target_ip}", "-w", "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running Gobuster: {e}")
