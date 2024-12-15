from Modules.Imports.protocol_imports import *

def http_submenu(target_ip, open_ports):
    actions = {
        "1": {"description": "Run WhatWeb", "function": run_whatweb},
        "2": {"description": "Run Gobuster", "function": run_gobuster},
        "3": {"description": "Run Dirb", "function": run_dirb},
        "4": {"description": "Run Nikto", "function": run_nikto},
        "5": {"description": "Run CEWL", "function": run_cewl},
        "6": {"description": "Run Dep-scan", "function": run_dep_scan},
        "7": {"description": "Run Davtest", "function": run_davtest},
        "8": {"description": "Run WPScan", "function": run_wpscan},
        "9": {"description": "Run Arjun", "function": run_arjun},
        "10": {"description": "Run Waybackurls", "function": run_waybackurls},
    }
    build_submenu("HTTP Enumeration", target_ip, actions, open_ports)

def run_whatweb(target_ip, open_ports):
    title = "WhatWeb"
    content = f"whatweb -a3 http://{target_ip} -v"
    run_command(title, content, target_ip, open_ports)

def run_gobuster(target_ip, open_ports):
    title = "Gobuster"
    content = (
        f"1. gobuster dir -u http://{target_ip} -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt\n"
        f"2. gobuster dir -u http://{target_ip} -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -x php,php3,html,txt -t 100 -k --no-error\n"
        f"3. gobuster dir -u http://{target_ip} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 30 --timeout 1m --no-error\n"
        f"4. gobuster vhost -u http://{target_ip} -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt --append-domain -r -t 40 --no-error | grep \"Status: 200\""
    )
    run_command(title, content, target_ip, open_ports)

def run_dirb(target_ip, open_ports):
    title = "Dirb"
    content = f"dirb http://{target_ip} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt | grep CODE:200"
    run_command(title, content, target_ip, open_ports)

def run_nikto(target_ip, open_ports):
    title = "Nikto"
    content = f"nikto -host http://{target_ip}"
    run_command(title, content, target_ip, open_ports)

def run_cewl(target_ip, open_ports):
    title = "CEWL"
    content = f"cewl http://{target_ip} -w words.txt"
    run_command(title, content, target_ip, open_ports)

def run_dep_scan(target_ip, open_ports):
    title = "Dep-scan"
    content = f"depscan --src $PWD --reports-dir $PWD/reports"
    run_command(title, content, target_ip, open_ports)

def run_davtest(target_ip, open_ports):
    title = "Davtest"
    content = f"davtest -url http://{target_ip}"
    run_command(title, content, target_ip, open_ports)

def run_wpscan(target_ip, open_ports):
    title = "WPScan"
    content = f"wpscan --url http://{target_ip} --enumerate vp"
    run_command(title, content, target_ip, open_ports)

def run_arjun(target_ip, open_ports):
    title = "Arjun"
    content = f"arjun -u http://{target_ip}"
    run_command(title, content, target_ip, open_ports)

def run_waybackurls(target_ip, open_ports):
    title = "Waybackurls"
    content = f"echo http://{target_ip} | waybackurls"
    run_command(title, content, target_ip, open_ports)

def run_feroxbuster(target_ip, open_ports):
    title = "Feroxbuster"
    content = f"feroxbuster -u http://{target_ip} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 --silent\n"
    run_command(title, content, target_ip, open_ports)
