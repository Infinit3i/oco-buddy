import subprocess
from colorama import Fore, Style
import inspect
import importlib

from Assets.ascii_text_prompts import ascii_art, full_ascii_art, infinitei
from Modules.All_Pages.clear_screen import clear_screen
from Modules.All_Pages.random_tip import get_random_tip_with_color

from Modules.All_Pages.center_text import *

from Modules.Login.scan import BACKGROUND_TASK

def highlight_ports(port, open_ports): # Highlight a port if it is in the list of open ports.
    return f"{Fore.GREEN}{port}{Style.RESET_ALL}" if port in open_ports else f"{port}" 

def display_background_task():
    if BACKGROUND_TASK:
        print("\nBackground Task:")
        for task in BACKGROUND_TASK:
            print(f"  - {task}")
    else:
        print("\nBackground Task: None")

def header(target_ip, open_ports):
    clear_screen()
    print(center_text(ascii_art))  # Display the full ASCII art banner
    print(center_text(get_random_tip_with_color()) + "\n")
    print(center_text(f"Target IP: {target_ip}\n"))
    if open_ports:
        print(center_text(f"Open Ports: {', '.join(open_ports)}\n"))
    else:
        print(center_text("Open Ports: None\n"))

def build_dynamic_submenu(module, target_ip, open_ports):
    # Extract all functions in the original order of definition
    source = inspect.getsource(module)
    lines = source.splitlines()
    actions = {}
    
    # Find all function definitions in order
    for line in lines:
        if line.strip().startswith("def "):  # Identify function definitions
            func_name = line.strip().split(" ")[1].split("(")[0]
            func = getattr(module, func_name, None)
            if func and inspect.isfunction(func):
                actions[func_name] = func

    # Initialize action status tracker
    action_status = {key: False for key in actions}

    while True:
        # Display submenu header
        header(target_ip, open_ports)
        print(center_text(f"=== {module.__name__.split('.')[-1].upper()} Enumeration ==="))
        
        # List all actions dynamically in the order defined in the module
        for idx, (name, func) in enumerate(actions.items(), start=1):
            status = "✔️" if action_status[name] else "❌"
            print(f"[{idx}] {status} {name.replace('_', ' ').title()}")
        print("[C] Type Commands")
        print("[0] Back to Main Menu\n")

        # Menu selection
        choice = input("Select an option: ").strip().lower()
        if choice == "0":
            break
        elif choice == "c":
            global_command_handler()
        elif choice.isdigit() and 1 <= int(choice) <= len(actions):
            selected_func = list(actions.values())[int(choice) - 1]
            selected_func(target_ip, open_ports)
            action_status[list(actions.keys())[int(choice) - 1]] = True  # Mark as completed
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")


def run_command(title, content, target_ip, open_ports):
    header(target_ip, open_ports)  # Display the header at the top
    print(f"=== {title} ===")
    print(f"Executing: {content}\n")

    try:
        subprocess.run(content, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error executing command: {e}{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}Command not found: {content.split()[0]}{Style.RESET_ALL}")
    except Exception as ex:
        print(f"{Fore.RED}An unexpected error occurred: {ex}{Style.RESET_ALL}")
    finally:
        input("\nPress Enter to return...")

def global_command_handler():
    """
    Allows the user to execute arbitrary shell commands.
    Shows both stdout and stderr for the executed commands.
    """
    print("\nEntering Command Mode (type 'exit' to return to the menu)\n")
    while True:
        command = input(f"{Fore.YELLOW}Command > {Style.RESET_ALL}").strip()
        if command.lower() in ["exit", "quit"]:
            print("Exiting Command Mode...")
            break
        try:
            result = subprocess.run(command, shell=True, text=True, capture_output=True)
            
            # Display the standard output (stdout)
            if result.stdout:
                print(f"{Fore.GREEN}{result.stdout}{Style.RESET_ALL}")
            
            # Display the standard error (stderr)
            if result.stderr:
                print(f"{Fore.RED}Error:\n{result.stderr}{Style.RESET_ALL}")
        
        except Exception as ex:
            print(f"{Fore.RED}An unexpected error occurred: {ex}{Style.RESET_ALL}")


def display_protocol_menu(target_ip, open_ports, menu_options):
    while True:
        header(target_ip, open_ports)
        print("\n=== MAIN Menu ===")
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
        build_dynamic_submenu(module, target_ip, open_ports)
    except ModuleNotFoundError:
        print(f"{Fore.RED}Error: Protocol module '{protocol}' not found.{Style.RESET_ALL}")
    except Exception as ex:
        print(f"{Fore.RED}An unexpected error occurred: {ex}{Style.RESET_ALL}")
