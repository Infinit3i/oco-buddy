from Modules.Imports.protocol_imports import *
import re
import webbrowser


def notes(target_ip, open_ports):
    title = "Notes"
    content = f"""
HTTP Notes:
  - Check robots.txt
  - Check for hidden directories
  - Check for hidden files
  - Check versions
"""
    run_command(title, content, target_ip, open_ports)


def whatweb(target_ip, open_ports):
    title = "WhatWeb"
    content = f"whatweb -a3 http://{target_ip} -v"
    run_command(title, content, target_ip, open_ports)


def robots(target_ip, open_ports):
    title = "Robots.txt"
    content = f"wget http://{target_ip}/robots.txt"
    run_command(title, content, target_ip, open_ports)
    
    
def feroxbuster(target_ip, open_ports):
    title = "Feroxbuster"
    content = f"feroxbuster -u http://{target_ip} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 --silent"
    run_command(title, content, target_ip, open_ports)
    
    
def skipfish(target_ip, open_ports):
    category = "http"
    title = "Skipfish"
    content = f"skipfish -k 00:06:00 -o doctorScan/ http://{target_ip}/"
    run_command(title, content, target_ip, open_ports)


def gobuster(target_ip, open_ports):
    title = "Gobuster"
    content = f"gobuster dir -u http://{target_ip} -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt > /tmp/gobuster.txt"
    run_command(title, content, target_ip, open_ports)


def wfuzz(target_ip, open_ports):
    title = "wfuzz"
    wordlist = "/usr/share/seclists/Discovery/Web-Content/common.txt"
    content = f'wfuzz -c -t 200 --hc=404 -H "User-Agent: h4x0r" -w {wordlist} http://{target_ip}/FUZZ'
    
    # Define a secondary action to open matching URLs in the browser
    def open_in_browser(output):
        # Regex to match URLs with 200 or 301 status codes
        matches = re.findall(r"http://[^\s]+ \(200\)|http://[^\s]+ \(301\)", output)
        for match in matches:
            url = match.split(" ")[0]
            print(f"[INFO] Opening: {url}")
            webbrowser.open(url)

    run_command(title, content, target_ip, open_ports, open_in_browser)


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