from Modules.Imports.protocol_imports import *

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


dns_commands = {
    "run_dig": {
        "category": "dns",
        "title": "dig",
        "content": lambda target_ip: f"dig {target_ip}"
    },
    "run_nslookup": {
        "category": "dns",
        "title": "nslookup",
        "content": lambda target_ip: f"nslookup {target_ip}"
    },
    "run_zone_transfer": {
        "category": "dns",
        "title": "Zone Transfer",
        "content": lambda target_ip: (
            f"dig axfr @{target_ip}\n"
            f"nslookup -type=any -query=AXFR {target_ip}"
        )
    },
    "run_gobuster_dns": {
        "category": "dns",
        "title": "Gobuster DNS",
        "content": lambda target_ip: (
            f"gobuster dns -d <domain> -w /usr/share/wordlists/dns/subdomains-top1million-5000.txt -r {target_ip}"
        )
    },
    "run_dnsrecon": {
        "category": "dns",
        "title": "dnsrecon",
        "content": lambda target_ip: f"dnsrecon -d <domain> -r {target_ip}"
    },
    "run_fierce": {
        "category": "dns",
        "title": "fierce",
        "content": lambda target_ip: f"fierce -dns <domain> -t {target_ip}"
    },
}
