import subprocess
from colorama import Fore, Style
import inspect
import importlib
import threading

from Assets.ascii_text_prompts import ascii_art
from Modules.UI.clear_screen import clear_screen
from Modules.UI.random_tip import get_random_tip_with_color
from Modules.UI.center_text import center_text
from Modules.Login.scan import BACKGROUND_TASK


def highlight_ports(port, open_ports): # Highlight a port if it is in the list of open ports.
    return f"{Fore.GREEN}{port}{Style.RESET_ALL}" if port in open_ports else f"{port}" 


def header(target_ip, open_ports):
    clear_screen()
    print(center_text(ascii_art))  # Display the full ASCII art banner
    print(center_text(get_random_tip_with_color()) + "\n")
    print(center_text(f"Target IP: {target_ip}\n"))
    if open_ports:
        print(center_text(f"Open Ports: {', '.join(map(str, open_ports))}\n"))
    else:
        print(center_text("Open Ports: None\n"))
    if BACKGROUND_TASK:
        print(center_text("Background Commands:"))
        for task in BACKGROUND_TASK:
            print(center_text(f"- {task}"))
        print()  # Add spacing
    else:
        print(center_text("Background Commands: None\n"))


def run_background_command(content, task_name):
    def task():
        try:
            subprocess.run(content, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Error executing background task '{task_name}': {e}{Style.RESET_ALL}")
        finally:
            # Remove task from BACKGROUND_TASK once done
            if task_name in BACKGROUND_TASK:
                BACKGROUND_TASK.remove(task_name)
    
    # Add task to BACKGROUND_TASK and run in a thread
    BACKGROUND_TASK.append(task_name)
    threading.Thread(target=task, daemon=True).start()


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
    print("=" * 40)
    print(f"{title.center(40)}")
    print("\n")

    try:
        # Execute the command and display its output in real-time
        subprocess.run(content, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command:\n{e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
    finally:
        input("\nPress Enter to return...")
      
""" i want to have this replace the current run function so i can have all of the protocol files dictionaries
def execute_protocol_command(protocol_commands, command_key, target_ip, open_ports):
    if command_key in protocol_commands:
        command = protocol_commands[command_key]
        category = command["category"]
        title = command["title"]
        content = command["content"](target_ip)  # Generate the content dynamically
        
        # Check if the ports match before executing
        if any(port in open_ports for port in category["ports"]):
            run_command(category["protocol"], title, content, target_ip, open_ports)
        else:
            print(f"{Fore.RED}Open ports do not match the required ports for {title}.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Command '{command_key}' not found.{Style.RESET_ALL}")
"""


def global_command_handler():
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
            print(f"[{key}] {option['name'].upper()}")
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
