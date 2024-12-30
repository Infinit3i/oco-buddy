from Modules.Imports.protocol_imports import *
import subprocess
import re
import webbrowser

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
    category = "http"
    title = "wfuzz"
    wordlist = "/usr/share/seclists/Discovery/Web-Content/common.txt"
    content = 'fuzz -c -t 200 --hc=404 -H "User-Agent: h4x0r" -w {wordlist} http://{target_ip}/FUZZ'
    
    try:
        # Run the wfuzz command and capture output
        run_command(title, content, target_ip, open_ports)
        result = subprocess.run(content, shell=True, capture_output=True, text=True, check=True)
        print(result.stdout)

        # Extract links with status code 200 or 301
        matches = re.findall(r"http://[^\s]+ \(200\)|http://[^\s]+ \(301\)", result.stdout)

        # Open each matching link in the browser
        if matches:
            print("\n[INFO] Found the following links:")
            for match in matches:
                url = match.split(" ")[0]  # Extract the URL part before the status code
                print(f"Opening: {url}")
                webbrowser.open(url)
        else:
            print("[INFO] No links with status code 200 or 301 found.")

    except subprocess.CalledProcessError as e:
        print(f"Error running wfuzz:\n{e}")


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