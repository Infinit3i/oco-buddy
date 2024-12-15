from Modules.Imports.protocol_imports import *

def run_snmpwalk(target_ip, open_ports):
    title = "SNMP Walk"
    content = f"snmpwalk -c public -v1 {target_ip}"
    run_command(title, content, target_ip, open_ports)

def run_snmpcheck(target_ip, open_ports):
    title = "SNMP Check"
    content = f"snmpcheck -t {target_ip} -c public"
    run_command(title, content, target_ip, open_ports)

def run_onesixtyone(target_ip, open_ports):
    title = "onesixtyone"
    content = f"onesixtyone -c community_names.txt -i {target_ip}"
    run_command(title, content, target_ip, open_ports)

def run_nmap_snmp(target_ip, open_ports):
    title = "Nmap SNMP Scripts"
    content = (
        f"nmap -sU -p 161 --script snmp-brute,snmp-info,snmp-netstat,snmp-processes {target_ip}"
    )
    run_command(title, content, target_ip, open_ports)

def run_snmpenum(target_ip, open_ports):
    title = "SNMPEnum"
    content = f"snmpenum -t {target_ip}"
    run_command(title, content, target_ip, open_ports)

def run_snmp_brute(target_ip, open_ports):
    title = "SNMP Brute-Force"
    content = f"nmap -sU -p 161 --script snmp-brute {target_ip}"
    run_command(title, content, target_ip, open_ports)

def show_hacktricks_reference(target_ip, open_ports):
    title = "HackTricks Reference"
    content = (
        f"Visit the following link for more SNMP enumeration tips:\n\n"
        f"https://book.hacktricks.xyz/network-services-pentesting/pentesting-snmp"
    )
    run_command(title, content, target_ip, open_ports)
