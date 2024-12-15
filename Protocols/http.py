from Modules.Imports.protocol_imports import *

def run_whatweb(target_ip, open_ports):
    title = "WhatWeb"
    content = f"whatweb -a3 http://{target_ip} -v"
    run_command(title, content, target_ip, open_ports)
    
def run_feroxbuster(target_ip, open_ports):
    title = "Feroxbuster"
    content = f"feroxbuster -u http://{target_ip} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 --silent"
    run_command(title, content, target_ip, open_ports)
    
def run_skipfish(target_ip, open_ports):
    """Run Skipfish for web application security scanning."""
    title = "Skipfish"
    content = f"skipfish -k 00:06:00 -o doctorScan/ http://{target_ip}/"
    run_command(title, content, target_ip, open_ports)

def run_gobuster(target_ip, open_ports):
    title = "Gobuster"
    content = f"1. gobuster dir -u http://{target_ip} -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt"
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

