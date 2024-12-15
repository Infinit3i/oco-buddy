from Modules.Imports.protocol_imports import *

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
