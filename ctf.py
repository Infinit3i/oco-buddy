from Modules.Login.check_ip import get_target_ip, get_box_name
from Modules.Login.scan import scan_ports
from Protocols.menu import protocol_menu

if __name__ == "__main__":
    box_name = get_box_name()
    target_ip = get_target_ip()
    if target_ip:
        OPEN_PORTS = scan_ports(target_ip, box_name)
        protocol_menu(target_ip, OPEN_PORTS)