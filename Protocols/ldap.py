from Modules.Imports.protocol_imports import *

def ldap_submenu(target_ip, open_ports):
    actions = {
        "1": {"description": "Enumerate LDAP with ldapsearch", "function": run_ldapsearch},
        "2": {"description": "Enumerate LDAP with windapsearch", "function": run_windapsearch},
        "3": {"description": "Enumerate LDAP with ldapdomaindump", "function": run_ldapdomaindump},
        "4": {"description": "Use Nmap Scripts for LDAP", "function": run_nmap_ldap},
        "5": {"description": "HackTricks Reference", "function": show_hacktricks_reference},
    }
    build_submenu("LDAP Enumeration", target_ip, actions, open_ports)

def run_ldapsearch(target_ip, open_ports):
    title = "ldapsearch"
    content = (
        f"ldapsearch -x -H ldap://{target_ip} -b 'dc=example,dc=com'"
    )
    run_command(title, content, target_ip, open_ports)

def run_windapsearch(target_ip, open_ports):
    title = "windapsearch.py"
    content = (
        f"python3 windapsearch.py --dc-ip {target_ip} -u USER@DOMAIN -p PASSWORD --computers"
    )
    run_command(title, content, target_ip, open_ports)

def run_ldapdomaindump(target_ip, open_ports):
    title = "ldapdomaindump"
    content = (
        f"ldapdomaindump ldap://{target_ip} -u 'DOMAIN\\USER' -p 'PASSWORD'"
    )
    run_command(title, content, target_ip, open_ports)

def run_nmap_ldap(target_ip, open_ports):
    title = "Nmap LDAP Scripts"
    content = (
        f"nmap -p 389 --script ldap-search,ldap-brute,ldap-novell-getpass {target_ip}"
    )
    run_command(title, content, target_ip, open_ports)

def show_hacktricks_reference(target_ip, open_ports):
    title = "HackTricks Reference"
    content = (
        f"Visit the following link for more LDAP enumeration tips:\n\n"
        f"https://book.hacktricks.xyz/network-services-pentesting/pentesting-ldap"
    )
    run_command(title, content, target_ip, open_ports)
