from Modules.Imports.protocol_imports import *

def oracle_submenu(target_ip, open_ports):
    actions = {
        "1": {"description": "Check Version with tnscmd10g", "function": run_tnscmd_version},
        "2": {"description": "Check Status with tnscmd10g", "function": run_tnscmd_status},
        "3": {"description": "Enumerate with Nmap Scripts", "function": run_nmap_oracle_scripts},
        "4": {"description": "Test Default Credentials with Metasploit", "function": test_default_credentials},
        "5": {"description": "Enumerate SID with ODAT (Oracle Database Attacking Tool)", "function": enumerate_sid_with_odat},
        "6": {"description": "Brute-Force Login with ODAT", "function": brute_force_oracle_odat},
        "7": {"description": "HackTricks Reference", "function": show_hacktricks_reference},
    }
    build_submenu("Oracle Enumeration", target_ip, actions, open_ports)

def run_tnscmd_version(target_ip, open_ports):
    title = "Check Version with tnscmd10g"
    content = f"tnscmd10g version -h {target_ip}"
    run_command(title, content, target_ip, open_ports)

def run_tnscmd_status(target_ip, open_ports):
    title = "Check Status with tnscmd10g"
    content = f"tnscmd10g status -h {target_ip}"
    run_command(title, content, target_ip, open_ports)

def run_nmap_oracle_scripts(target_ip, open_ports):
    title = "Nmap Oracle Scripts"
    content = (
        f"nmap -p 1521 --script oracle-brute,oracle-enum-users,oracle-sid-brute,oracle-tns-version {target_ip}"
    )
    run_command(title, content, target_ip, open_ports)

def test_default_credentials(target_ip, open_ports):
    title = "Test Default Credentials with Metasploit"
    content = (
        f"use auxiliary/scanner/oracle/oracle_login\n"
        f"set RHOSTS {target_ip}\n"
        f"set USERNAME SYS\n"
        f"set PASSWORD SYS\n"
        f"run"
    )
    run_command(title, content, target_ip, open_ports)

def enumerate_sid_with_odat(target_ip, open_ports):
    title = "Enumerate SID with ODAT"
    content = f"odat sidguesser -s {target_ip} -p 1521"
    run_command(title, content, target_ip, open_ports)

def brute_force_oracle_odat(target_ip, open_ports):
    title = "Brute-Force Login with ODAT"
    content = f"odat passwordguesser -s {target_ip} -p 1521 -d <SID> -U usernames.txt -P passwords.txt"
    run_command(title, content, target_ip, open_ports)

def show_hacktricks_reference(target_ip, open_ports):
    title = "HackTricks Reference"
    content = (
        f"Visit the following link for more Oracle enumeration tips:\n\n"
        f"https://book.hacktricks.xyz/network-services-pentesting/pentesting-oracle"
    )
    run_command(title, content, target_ip, open_ports)
