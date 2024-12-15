import importlib
from Modules.All_Pages.wrappers import build_dynamic_submenu

def display_protocol_menu(target_ip, open_ports, menu_options):
    while True:
        print("\n=== Protocol Enumeration Menu ===")
        for key, option in menu_options.items():
            protocol_ports = "/".join(option["ports"])
            print(f"[{key}] {option['name'].upper()} (Ports: {protocol_ports})")
        print("[0] Exit\n")

        choice = input("Select a protocol: ").strip()
        if choice == "0":
            print("Exiting...")
            break
        elif choice in menu_options:
            protocol = menu_options[choice]["name"]
            load_and_run_protocol(protocol, target_ip, open_ports)
        else:
            print("Invalid choice. Please try again.")

def load_and_run_protocol(protocol, target_ip, open_ports):
    try:
        # Import the protocol module dynamically
        module = importlib.import_module(f"Protocols.{protocol}")
        print(f"\n=== {protocol.upper()} Enumeration ===")
        build_dynamic_submenu(module, target_ip, open_ports)
    except ModuleNotFoundError:
        print(f"Error: Protocol module '{protocol}' not found.")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
