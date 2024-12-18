from Modules.Imports.protocol_imports import *

def robots(target_ip, open_ports):
    title = "Robots.txt"
    content = f"wget http://{target_ip}/robots.txt"
    run_command(title, content, target_ip, open_ports)

def whatweb(target_ip, open_ports):
    title = "WhatWeb"
    content = f"whatweb -a3 http://{target_ip} -v"
    run_command(title, content, target_ip, open_ports)
    
def feroxbuster(target_ip, open_ports):
    title = "Feroxbuster"
    content = f"feroxbuster -u http://{target_ip} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 --silent"
    run_command(title, content, target_ip, open_ports)
    
def skipfish(target_ip, open_ports):
    title = "Skipfish"
    content = f"skipfish -k 00:06:00 -o doctorScan/ http://{target_ip}/"
    run_command(title, content, target_ip, open_ports)

def gobuster(target_ip, open_ports):
    title = "Gobuster"
    content = f"1. gobuster dir -u http://{target_ip} -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt"
    run_command(title, content, target_ip, open_ports)

def dirb(target_ip, open_ports):
    title = "Dirb"
    content = f"dirb http://{target_ip} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt | grep CODE:200"
    run_command(title, content, target_ip, open_ports)

def cewl(target_ip, open_ports):
    title = "CEWL"
    content = f"cewl http://{target_ip} -w words.txt"
    run_command(title, content, target_ip, open_ports)

def nikto(target_ip, open_ports):
    title = "Nikto"
    content = f"nikto -host http://{target_ip}"
    run_command(title, content, target_ip, open_ports)
    
def dep_scan(target_ip, open_ports):
    title = "Dep-scan"
    content = f"depscan --src $PWD --reports-dir $PWD/reports"
    run_command(title, content, target_ip, open_ports)

def davtest(target_ip, open_ports):
    title = "Davtest"
    content = f"davtest -url http://{target_ip}"
    run_command(title, content, target_ip, open_ports)

def wpscan(target_ip, open_ports):
    title = "WPScan"
    content = f"wpscan --url http://{target_ip} --enumerate vp"
    run_command(title, content, target_ip, open_ports)

def arjun(target_ip, open_ports):
    title = "Arjun"
    content = f"arjun -u http://{target_ip}"
    run_command(title, content, target_ip, open_ports)

def waybackurls(target_ip, open_ports):
    title = "Waybackurls"
    content = f"echo http://{target_ip} | waybackurls"
    run_command(title, content, target_ip, open_ports)

