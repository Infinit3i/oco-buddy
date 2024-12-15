from Modules.Imports.protocol_imports import *

def dns_submenu(target_ip, open_ports):
    actions = {
        "1": {"description": "Run dig", "function": run_dig},
        "2": {"description": "Run nslookup", "function": run_nslookup},
        "3": {"description": "Enumerate DNS zone (zone transfer)", "function": run_zone_transfer},
        "4": {"description": "Test subdomain brute-forcing with gobuster", "function": run_gobuster_dns},
        "5": {"description": "Enumerate with dnsrecon", "function": run_dnsrecon},
        "6": {"description": "Enumerate with fierce", "function": run_fierce},
    }
    build_submenu("DNS Enumeration", target_ip, actions, open_ports)

def run_dig(target_ip, open_ports):
    title = "dig"
    content = f"dig {target_ip}"
    run_command(title, content, target_ip, open_ports)

def run_nslookup(target_ip, open_ports):
    title = "nslookup"
    content = f"nslookup {target_ip}"
    run_command(title, content, target_ip, open_ports)

def run_zone_transfer(target_ip, open_ports):
    title = "Zone Transfer"
    content = (
        f"dig axfr @{target_ip}\n"
        f"nslookup -type=any -query=AXFR {target_ip}"
    )
    run_command(title, content, target_ip, open_ports)

def run_gobuster_dns(target_ip, open_ports):
    title = "Gobuster DNS"
    content = (
        f"gobuster dns -d <domain> -w /usr/share/wordlists/dns/subdomains-top1million-5000.txt -r {target_ip}"
    )
    run_command(title, content, target_ip, open_ports)

def run_dnsrecon(target_ip, open_ports):
    title = "dnsrecon"
    content = f"dnsrecon -d <domain> -r {target_ip}"
    run_command(title, content, target_ip, open_ports)

def run_fierce(target_ip, open_ports):
    title = "fierce"
    content = f"fierce -dns <domain> -t {target_ip}"
    run_command(title, content, target_ip, open_ports)
