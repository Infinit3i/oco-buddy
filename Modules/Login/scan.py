import os
import subprocess
import sys
from datetime import datetime
import threading

# Define the global SAVED_DIR variable
SAVED_DIR = "SAVED"
os.makedirs(SAVED_DIR, exist_ok=True)  # Create the directory if it doesn't exist
# Global list to store background tasks
BACKGROUND_TASK = []

def ensure_saved_directory():
    """
    Ensures that the SAVED directory exists.
    """
    global SAVED_DIR
    SAVED_DIR = "SAVED"  # Define the SAVED directory globally
    os.makedirs(SAVED_DIR, exist_ok=True)  # Create the directory if it doesn't exist


def scan_ports(target_ip, box_name):
    ensure_saved_directory()  # Ensure SAVED directory exists

    print(f"Scanning {target_ip} for open ports (Fast scan)...")
    try:
        box_path = os.path.join(SAVED_DIR, box_name)
        os.makedirs(box_path, exist_ok=True)  # Create folder for box results

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

        # Save the quick scan results
        quick_scan_file = os.path.join(box_path, f"{target_ip}-quick.txt")
        with open(quick_scan_file, "w") as file:
            file.write(output)
        print(f"Quick scan results saved to {quick_scan_file}")
        
        # Add detailed Nmap scan to background tasks
        BACKGROUND_TASK.append(f"Nmap -sVC {target_ip}")
        threading.Thread(target=detailed_scan, args=(target_ip, box_name), daemon=True).start()

        return open_ports
    except subprocess.CalledProcessError as e:
        print(f"Error running Nmap: {e.stderr}")


def detailed_scan(target_ip, box_name):
    current_date = datetime.now().strftime("%Y-%m-%d")
    box_path = os.path.join(SAVED_DIR, box_name)
    os.makedirs(box_path, exist_ok=True)
    output_file_base = os.path.join(box_path, f"{target_ip}-{current_date}")
    try:
        subprocess.run(
            ["nmap", "-sVC", target_ip, "-oA", output_file_base], check=True
        )
        print(f"Detailed scan results saved to {output_file_base}.nmap/.xml/.gnmap")
    except subprocess.CalledProcessError as e:
        print(f"Error running detailed Nmap scan: {e}")
