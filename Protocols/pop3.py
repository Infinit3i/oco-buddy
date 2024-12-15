from Modules.Imports.protocol_imports import *

def manual_pop3_enumeration(target_ip, open_ports):
    title = "Manual POP3 Enumeration via Telnet"
    content = (
        f"telnet {target_ip} 110\n\n"
        f"Commands:\n"
        f"USER <username>\n"
        f"PASS <password>\n"
        f"LIST  # List messages\n"
        f"RETR <#>  # Retrieve a message\n"
        f"QUIT  # Exit"
    )
    run_command(title, content, target_ip, open_ports)

def run_nmap_pop3_scripts(target_ip, open_ports):
    title = "Nmap POP3 Scripts"
    content = f"nmap -p 110 --script pop3-capabilities,pop3-ntlm-info {target_ip}"
    run_command(title, content, target_ip, open_ports)

def run_hydra_pop3(target_ip, open_ports):
    title = "Hydra POP3 Brute-Force"
    content = f"hydra -l USERNAME -P /usr/share/wordlists/rockyou.txt {target_ip} pop3"
    run_command(title, content, target_ip, open_ports)

def test_weak_passwords(target_ip, open_ports):
    title = "Test Weak Passwords"
    content = (
        f"Common credentials to test:\n\n"
        f"Username: admin, Password: admin\n"
        f"Username: user, Password: password\n"
        f"Username: guest, Password: guest\n\n"
        f"Command: telnet {target_ip} 110"
    )
    run_command(title, content, target_ip, open_ports)

def show_hacktricks_reference(target_ip, open_ports):
    title = "HackTricks Reference"
    content = (
        f"Visit the following link for more POP3 enumeration tips:\n\n"
        f"https://book.hacktricks.xyz/network-services-pentesting/pentesting-pop3"
    )
    run_command(title, content, target_ip, open_ports)
