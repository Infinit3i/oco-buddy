from Modules.Imports.protocol_imports import *

def run_nmap_ftp_scripts(target_ip, open_ports):
    title = "Nmap FTP Scripts"
    content = (
        f"nmap --script ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,"
        f"ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221,tftp-enum -p 21 {target_ip}"
    )
    run_command(title, content, target_ip, open_ports)

def run_nmap_version_scan(target_ip, open_ports):
    title = "Nmap FTP Version Scan"
    content = f"sudo nmap -sV -p21 -sC -A {target_ip}"
    run_command(title, content, target_ip, open_ports)

def test_anonymous_login(target_ip, open_ports):
    title = "Test Anonymous Login"
    content = (
        f"ftp {target_ip}\n"
        f"> anonymous\n"
        f"> anonymous\n"
        f"> ls -a # List all files (even hidden)\n"
        f"> binary # Set transmission to binary\n"
        f"> ascii # Set transmission to ASCII\n"
        f"> bye # Exit"
    )
    run_command(title, content, target_ip, open_ports)

def manual_ftp_enumeration(target_ip, open_ports):
    title = "Manual FTP Enumeration"
    content = (
        f"Connect to FTP server using:\n\n"
        f"ftp {target_ip}\n\n"
        f"Commands:\n"
        f"- anonymous : anonymous\n"
        f"- ftp : ftp\n"
        f"> ls -a (list all files, even hidden)\n"
        f"> binary (set transmission to binary)\n"
        f"> ascii (set transmission to ASCII)"
    )
    run_command(title, content, target_ip, open_ports)

def run_hydra_ftp(target_ip, open_ports):
    title = "Hydra FTP Brute-Force"
    content = f"hydra -l anonymous -P /usr/share/wordlists/rockyou.txt ftp://{target_ip}"
    run_command(title, content, target_ip, open_ports)

def run_medusa_ftp(target_ip, open_ports):
    title = "Medusa FTP Brute-Force"
    content = f"medusa -h {target_ip} -u anonymous -P /usr/share/wordlists/rockyou.txt -M ftp"
    run_command(title, content, target_ip, open_ports)

def enumerate_ftp_files_curlftpfs(target_ip, open_ports):
    title = "Enumerate FTP Files with curlftpfs"
    content = (
        f"curlftpfs anonymous:anonymous@{target_ip} /mnt/ftp\n"
        f"ls -la /mnt/ftp\n"
        f"fusermount -u /mnt/ftp"
    )
    run_command(title, content, target_ip, open_ports)

def show_hacktricks_reference(target_ip, open_ports):
    title = "HackTricks Reference"
    content = (
        f"Visit the following link for more FTP enumeration tips:\n\n"
        f"https://book.hacktricks.xyz/network-services-pentesting/pentesting-ftp"
    )
    run_command(title, content, target_ip, open_ports)
