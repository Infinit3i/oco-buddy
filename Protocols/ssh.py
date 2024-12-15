from Modules.Imports.protocol_imports import *

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
