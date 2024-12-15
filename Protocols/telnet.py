from Modules.Imports.protocol_imports import *

def check_banner(target_ip, open_ports):
    title = "Check Telnet Banner"
    content = (
        f"Command to check Telnet banner:\n"
        f"telnet {target_ip} 23\n"
        f"Manually observe the response for version information."
    )
    run_command(title, content, target_ip, open_ports)

def attempt_anonymous_login(target_ip, open_ports):
    title = "Attempt Anonymous Login"
    content = (
        f"Attempting Telnet login with common credentials:\n"
        f"- USER: admin | PASSWORD: admin\n"
        f"- USER: root  | PASSWORD: root\n\n"
        f"Command:\n"
        f"telnet {target_ip} 23\n"
        f"USER: anonymous | PASSWORD: (leave blank)"
    )
    run_command(title, content, target_ip, open_ports)

def brute_force_credentials(target_ip, open_ports):
    title = "Brute-Force Telnet Credentials"
    content = (
        f"Use Hydra for Telnet brute-forcing:\n\n"
        f"Command:\n"
        f"hydra -L users.txt -P passwords.txt telnet://{target_ip}\n"
        f"Replace 'users.txt' and 'passwords.txt' with appropriate wordlists."
    )
    run_command(title, content, target_ip, open_ports)

def test_command_execution(target_ip, open_ports):
    title = "Test for Command Execution"
    content = (
        f"Test Telnet for command execution:\n"
        f"1. Connect to Telnet:\n"
        f"   telnet {target_ip} 23\n"
        f"2. Try executing basic commands (e.g., id, uname -a)."
    )
    run_command(title, content, target_ip, open_ports)

def enumerate_telnet_services(target_ip, open_ports):
    title = "Enumerate Telnet Services"
    content = (
        f"Use Nmap for service enumeration:\n\n"
        f"Command:\n"
        f"nmap -p 23 --script telnet-encryption,telnet-brute {target_ip}\n\n"
        f"These scripts can test for encryption and brute-force attempts."
    )
    run_command(title, content, target_ip, open_ports)

def exploit_telnet_vulnerabilities(target_ip, open_ports):
    title = "Exploit Telnet Vulnerabilities"
    content = (
        f"Check for known Telnet vulnerabilities:\n\n"
        f"Command:\n"
        f"nmap --script telnet-vuln* -p 23 {target_ip}\n\n"
        f"Examples:\n"
        f"- CVE-2011-4862: Telnet DoS Vulnerability\n"
        f"- CVE-2020-10188: Telnet remote code execution\n\n"
        f"Use Metasploit:\n"
        f"msfconsole\n"
        f"use auxiliary/scanner/telnet/telnet_login\n"
        f"set RHOSTS {target_ip}\n"
        f"run"
    )
    run_command(title, content, target_ip, open_ports)
