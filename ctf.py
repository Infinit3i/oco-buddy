from Modules.Imports.all_imports import *
from Protocols.menu import MENU_OPTIONS as BASE_MENU_OPTIONS

if __name__ == "__main__":
    box_name = get_box_name()
    target_ip = get_target_ip()  # Ask for the IP before anything else
    if target_ip:  # Ensure the IP is valid before proceeding
        OPEN_PORTS = scan_ports(target_ip, box_name)  # Pass the valid IP and capture open ports

        # Update MENU_OPTIONS to pass necessary arguments
        MENU_OPTIONS = {
            key: {
                **value,
                "submenu": value["submenu"],  # Pass the actual function
            }
            for key, value in BASE_MENU_OPTIONS.items()
        }

        display_menu(MENU_OPTIONS, OPEN_PORTS, target_ip)  # Display the dynamic menu
