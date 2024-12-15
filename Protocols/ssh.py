from Modules.Imports.protocol_imports import *

def ssh_submenu(target_ip, open_ports):
    actions = {
        "1": {"description": "Find files owned by specific user", "function": find_user_files},
        "2": {"description": "Find 'root.txt' file", "function": find_root_file},
        "3": {"description": "List SETUID/SETGID files", "function": list_setuid_files},
        "4": {"description": "Check writable config files", "function": check_writable_files},
        "5": {"description": "Grep for passwords in /etc/", "function": grep_passwords},
        "6": {"description": "Run LinEnum.sh", "function": lin_enum},
    }
    build_submenu("SSH Enumeration", target_ip, actions, open_ports)


def find_user_files(target_ip, open_ports):
    title = "Find Files Owned by User"
    content = f"find / -uid <USER UUID> -type f -ls 2>/dev/null | grep -v '/proc*'"
    run_command(title, content, target_ip, open_ports)

def find_root_file(target_ip, open_ports):
    title = "Find 'root.txt' File"
    content = f"find / -name 'root.txt' -exec cat {{}} \\; 2>/dev/null"
    run_command(title, content, target_ip, open_ports)

def list_setuid_files(target_ip, open_ports):
    title = "List SETUID/SETGID Files"
    content = f"find / -perm -4000 -o -perm -2000 -ls 2>/dev/null"
    run_command(title, content, target_ip, open_ports)

def check_writable_files(target_ip, open_ports):
    title = "Check Writable Config Files"
    content = f"find /etc -perm -2"
    run_command(title, content, target_ip, open_ports)

def grep_passwords(target_ip, open_ports):
    title = "Grep for Passwords in /etc/"
    content = f"grep -Inri passw /etc/* 2>/dev/null"
    run_command(title, content, target_ip, open_ports)

def lin_enum(target_ip, open_ports):
    title = "Run LinEnum.sh"
    content = (
        f"Download and execute LinEnum.sh from:\n"
        f"https://github.com/rebootuser/LinEnum\n\n"
    )
    run_command(title, content, target_ip, open_ports)
