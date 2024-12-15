from Modules.Imports.all_imports import *

# Global variable to store open ports
OPEN_PORTS = []

MENU_OPTIONS = {
    "1": {"name": "http", "ports": ["80", "443"], "submenu": http_submenu},
    "2": {"name": "ssh", "ports": ["22"], "submenu": ssh_submenu},
    "3": {"name": "rpc/smb", "ports": ["135", "445"], "submenu": rpc_smb_submenu},
    "4": {"name": "ftp", "ports": ["21"], "submenu": ftp_submenu},
    "5": {"name": "telnet", "ports": ["23"], "submenu": telnet_submenu},
    "6": {"name": "dns", "ports": ["53"], "submenu": dns_submenu},
    "7": {"name": "finger", "ports": ["79"], "submenu": finger_submenu},
    "8": {"name": "kerberos", "ports": ["88"], "submenu": kerberos_submenu},
    "9": {"name": "pop3", "ports": ["110"], "submenu": pop3_submenu},
    "10": {"name": "snmp", "ports": ["161"], "submenu": snmp_submenu},
    "11": {"name": "ldap", "ports": ["389"], "submenu": ldap_submenu},
    "12": {"name": "mssql", "ports": ["1433"], "submenu": mssql_submenu},
    "13": {"name": "oracle", "ports": ["1521"], "submenu": oracle_submenu},
    "14": {"name": "mysql", "ports": ["3306"], "submenu": mysql_submenu},
    "15": {"name": "docker", "ports": ["5000"], "submenu": docker_submenu},
    "16": {"name": "winrm", "ports": ["5985", "5986"], "submenu": winrm_submenu},
    "17": {"name": "mongodb", "ports": ["27017"], "submenu": mongodb_submenu},
}