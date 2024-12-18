from Modules.All_Pages.wrappers import display_protocol_menu

# Global variable to store dynamically added protocols
OPEN_PORTS = {}

# Dynamic menu options (predefined protocols)
MENU_OPTIONS = {
    "1": {"name": "http", "ports": ["80", "443", "8080", "8000", "8443"]},  # Web services
    "2": {"name": "ssh", "ports": ["22"]},  # Secure Shell
    "3": {"name": "rpc_smb", "ports": ["135", "139", "445"]},  # SMB / RPC
    "4": {"name": "ftp", "ports": ["21"]},  # FTP service
    "5": {"name": "telnet", "ports": ["23"]},  # Telnet
    "6": {"name": "dns", "ports": ["53"]},  # DNS
    "7": {"name": "finger", "ports": ["79"]},  # Finger
    "8": {"name": "kerberos", "ports": ["88"]},  # Kerberos
    "9": {"name": "smtp", "ports": ["25", "465", "587"]},  # SMTP
    "10": {"name": "pop3", "ports": ["110", "995"]},  # POP3
    "11": {"name": "imap", "ports": ["143", "993"]},  # IMAP
    "12": {"name": "snmp", "ports": ["161", "162"]},  # SNMP
    "13": {"name": "ldap", "ports": ["389", "636"]},  # LDAP
    "14": {"name": "mssql", "ports": ["1433", "1434"]},  # MSSQL
    "15": {"name": "oracle", "ports": ["1521"]},  # Oracle Database
    "16": {"name": "mysql", "ports": ["3306"]},  # MySQL
    "17": {"name": "docker", "ports": ["2375", "2376"]},  # Docker API
    "18": {"name": "winrm", "ports": ["5985", "5986"]},  # WinRM
    "19": {"name": "mongodb", "ports": ["27017"]},  # MongoDB
    "20": {"name": "nfs", "ports": ["111", "2049"]},  # NFS
    "21": {"name": "vnc", "ports": ["5900", "5901", "5902"]},  # VNC
    "22": {"name": "rdp", "ports": ["3389"]},  # Remote Desktop Protocol
    "23": {"name": "redis", "ports": ["6379"]},  # Redis service
    "24": {"name": "elasticsearch", "ports": ["9200", "9300"]},  # Elasticsearch
    "25": {"name": "kubernetes_api", "ports": ["6443"]},  # Kubernetes API
    "26": {"name": "rabbitmq", "ports": ["5672", "15672"]},  # RabbitMQ
    "27": {"name": "git", "ports": ["9418"]},  # Git service
    "28": {"name": "proxy", "ports": ["3128", "8080", "8888"]},  # Proxy services
    "29": {"name": "postgresql", "ports": ["5432"]},  # PostgreSQL
    "30": {"name": "teamviewer", "ports": ["5938"]},  # TeamViewer
    "31": {"name": "rpcbind", "ports": ["111"]},  # RPCBind
    "32": {"name": "tftp", "ports": ["69"]},  # TFTP
}

# Function to display protocols with detected open ports
def protocol_menu(target_ip, detected_ports):
    """
    Displays protocols based on detected open ports.
    If no ports match, show all available protocols.
    """
    matched_protocols = {}

    # Filter predefined protocols based on detected ports
    for key, value in MENU_OPTIONS.items():
        if any(port in detected_ports for port in value["ports"]):
            matched_protocols[key] = value

    # Display filtered or all protocols
    if matched_protocols:
        print("\nProtocols with Detected Ports:")
        display_protocol_menu(target_ip, detected_ports, {key: {"name": value["name"]} for key, value in matched_protocols.items()})
    else:
        print("\nNo detected ports matched. Showing all protocols:")
        display_protocol_menu(target_ip, detected_ports, {key: {"name": value["name"]} for key, value in MENU_OPTIONS.items()})