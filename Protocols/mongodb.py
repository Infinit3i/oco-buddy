from Modules.Imports.protocol_imports import *

def mongodb_submenu(target_ip, open_ports):
    actions = {
        "1": {"description": "Check for Open MongoDB Instances", "function": check_open_instances},
        "2": {"description": "List Databases", "function": list_databases},
        "3": {"description": "Dump Collections", "function": dump_collections},
        "4": {"description": "Check for Authentication Bypass", "function": check_authentication_bypass},
        "5": {"description": "Test for MongoDB RCE Exploit", "function": test_rce_exploit},
    }
    build_submenu("MongoDB Enumeration", target_ip, actions, open_ports)

def check_open_instances(target_ip, open_ports):
    title = "Check for Open MongoDB Instances"
    content = f"nmap -p 27017 --script mongodb-info {target_ip}"
    run_command(title, content, target_ip, open_ports)

def list_databases(target_ip, open_ports):
    title = "List MongoDB Databases"
    content = (
        f"Use `mongo` CLI:\n\n"
        f"1. Connect: mongo {target_ip}:27017\n"
        f"2. Run: show dbs"
    )
    run_command(title, content, target_ip, open_ports)

def dump_collections(target_ip, open_ports):
    title = "Dump Collections from MongoDB"
    content = (
        f"Use `mongoexport`:\n\n"
        f"mongoexport --host {target_ip} --db <database_name> --collection <collection_name> --out <output_file.json>"
    )
    run_command(title, content, target_ip, open_ports)

def check_authentication_bypass(target_ip, open_ports):
    title = "Check for Authentication Bypass"
    content = (
        f"Attempt to access the database without credentials:\n\n"
        f"mongo {target_ip}:27017 --eval \"db.stats()\""
    )
    run_command(title, content, target_ip, open_ports)

def test_rce_exploit(target_ip, open_ports):
    title = "Test for MongoDB RCE Exploit"
    content = (
        f"Use Metasploit or other tools to test RCE vulnerabilities:\n\n"
        f"msfconsole -q\n"
        f"search mongodb\n"
        f"use exploit/linux/misc/mongodb_target_rce\n"
        f"set RHOSTS {target_ip}\n"
        f"run"
    )
    run_command(title, content, target_ip, open_ports)
