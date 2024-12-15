import subprocess
from colorama import Fore, Style
import inspect
import importlib
import os

from Assets.ascii_text_prompts import ascii_art
from Modules.All_Pages.utils import ensure_directory_exists, save_action_status, load_action_status
from Modules.All_Pages.clear_screen import clear_screen
from Modules.All_Pages.random_tip import get_random_tip_with_color
from Modules.Login.check_ip import get_box_name

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

def build_dynamic_submenu(module, target_ip, open_ports, box_name):
    # Box directory setup
    box_dir = os.path.join("SAVED", box_name)
    ensure_directory_exists(box_dir)

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

    # Load saved action status or initialize a new one
    action_status_file = os.path.join(box_dir, f"{module.__name__.split('.')[-1]}_status.json")
    action_status = load_action_status(action_status_file, default={key: False for key in actions})

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
            # Save action status before exiting
            save_action_status(action_status_file, action_status)
            break
        elif choice == "c":
            global_command_handler()
        elif choice.isdigit() and 1 <= int(choice) <= len(actions):
            selected_func = list(actions.values())[int(choice) - 1]
            selected_func(target_ip, open_ports)
            action_status[list(actions.keys())[int(choice) - 1]] = True  # Mark as completed
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")


def run_command(title, content, target_ip, open_ports, box_name):
    """
    Executes a shell command, prints the output to the screen, and saves it to a file in the appropriate directory.
    :param title: Title of the command/task.
    :param content: Shell command to execute.
    :param target_ip: Target IP address.
    :param open_ports: List of open ports for reference.
    :param box_name: Directory where the results are saved.
    """
    # Define the output directory and file
    box_dir = os.path.join("SAVED", box_name)
    ensure_directory_exists(box_dir)
    output_file = os.path.join(box_dir, f"{title.replace(' ', '_').lower()}_output.txt")

    # Display the header
    header(target_ip, open_ports)
    print(f"=== {title} ===")
    print(f"Executing: {content}\n")

    try:
        # Execute the command and capture the output
        result = subprocess.run(content, shell=True, text=True, capture_output=True)
        
        # Print and save the output
        if result.stdout:
            print(f"{Fore.GREEN}{result.stdout}{Style.RESET_ALL}")
            with open(output_file, "w") as f:
                f.write(result.stdout)
        
        # Print and save errors if they occur
        if result.stderr:
            print(f"{Fore.RED}Error:\n{result.stderr}{Style.RESET_ALL}")
            with open(output_file, "a") as f:
                f.write("\n--- Errors ---\n")
                f.write(result.stderr)
        
        # Check the return code for success/failure
        if result.returncode != 0:
            print(f"{Fore.RED}Command failed with exit code {result.returncode}.{Style.RESET_ALL}")

    except Exception as ex:
        # Handle unexpected errors
        print(f"{Fore.RED}An unexpected error occurred: {ex}{Style.RESET_ALL}")
        with open(output_file, "a") as f:
            f.write(f"\n--- Unexpected Error ---\n{str(ex)}")
    finally:
        print(f"\nOutput saved to: {output_file}")
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


def display_protocol_menu(target_ip, open_ports, menu_options, box_name):
    """
    Displays the protocol menu dynamically and highlights protocols with detected open ports.
    Passes the box_name for saving progress and results.
    """
    while True:
        header(target_ip, open_ports)
        print("\n=== MAIN Menu ===")
        
        for key, option in menu_options.items():
            # Highlight the line if any of the protocol's ports are open
            protocol_ports = option["ports"]
            is_open = any(port in open_ports for port in protocol_ports)
            
            line_color = Fore.GREEN if is_open else Style.RESET_ALL
            detected_ports = "/".join([highlight_ports(port, open_ports) for port in protocol_ports])
            
            print(f"{line_color}[{key}] {option['name'].upper()} (Ports: {detected_ports}){Style.RESET_ALL}")
        
        print("[0] Exit\n")

        choice = input("Select a protocol: ").strip()
        if choice == "0":
            print("Exiting...")
            break
        elif choice in menu_options:
            protocol = menu_options[choice]["name"]
            load_and_run_protocol(protocol, target_ip, open_ports, box_name)
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

def load_and_run_protocol(protocol, target_ip, open_ports, box_name):
    """
    Dynamically loads and runs the protocol's module and submenu.
    Passes the box_name to preserve state and save results.
    """
    try:
        # Import the protocol module dynamically
        module = importlib.import_module(f"Protocols.{protocol}")
        build_dynamic_submenu(module, target_ip, open_ports, box_name)
    except ModuleNotFoundError:
        print(f"{Fore.RED}Error: Protocol module '{protocol}' not found.{Style.RESET_ALL}")
    except Exception as ex:
        print(f"{Fore.RED}An unexpected error occurred: {ex}{Style.RESET_ALL}")