from Modules.Imports.protocol_imports import *

def run_finger(target_ip, open_ports):
    title = "Finger"
    content = f"finger @{target_ip}"
    run_command(title, content, target_ip, open_ports)

def run_finger_user_enum(target_ip, open_ports):
    title = "Finger User Enum (pentestmonkey)"
    content = (
        f"./finger-user-enum.pl -U users.txt -t {target_ip}\n\n"
        f"Download and setup instructions:\nhttps://pentestmonkey.net/tools/user-enumeration/finger-user-enum"
    )
    run_command(title, content, target_ip, open_ports)

def run_nmap_finger(target_ip, open_ports):
    title = "Nmap Finger Enumeration"
    content = f"nmap -p 79 --script finger {target_ip}"
    run_command(title, content, target_ip, open_ports)
