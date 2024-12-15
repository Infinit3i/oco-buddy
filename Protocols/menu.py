from Modules.All_Pages.wrappers import display_protocol_menu

# Global variable to store open ports
OPEN_PORTS = []

# Dynamic menu options
MENU_OPTIONS = {
    "1": {"name": "http", "ports": ["80", "443"]},
    "2": {"name": "ssh", "ports": ["22"]},
    "3": {"name": "rpc_smb", "ports": ["135", "445"]},
    "4": {"name": "ftp", "ports": ["21"]},
    "5": {"name": "telnet", "ports": ["23"]},
    "6": {"name": "dns", "ports": ["53"]},
    "7": {"name": "finger", "ports": ["79"]},
    "8": {"name": "kerberos", "ports": ["88"]},
    "9": {"name": "pop3", "ports": ["110"]},
    "10": {"name": "snmp", "ports": ["161"]},
    "11": {"name": "ldap", "ports": ["389"]},
    "12": {"name": "mssql", "ports": ["1433"]},
    "13": {"name": "oracle", "ports": ["1521"]},
    "14": {"name": "mysql", "ports": ["3306"]},
    "15": {"name": "docker", "ports": ["5000"]},
    "16": {"name": "winrm", "ports": ["5985", "5986"]},
    "17": {"name": "mongodb", "ports": ["27017"]},
}

# Expose the main protocol menu function
def protocol_menu(target_ip, open_ports):
    display_protocol_menu(target_ip, open_ports, MENU_OPTIONS)
