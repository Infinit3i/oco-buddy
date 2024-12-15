import subprocess
from colorama import Fore, Style

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
    print(center_text(ascii_art))
    print(center_text(get_random_tip_with_color()) + "\n")
    print(center_text(f"Target IP: {target_ip}\n"))
    if open_ports:
        print(center_text(f"Open Ports: {', '.join(open_ports)}\n"))
    else:
        print(center_text("Open Ports: None\n"))
    display_background_task() # Include the background tasks section



def display_menu(menu_options, open_ports, target_ip):
    while True:
        header(target_ip, open_ports)  # Pass target_ip and open_ports to the header
        print("\nStandard Enumeration")
        for key, value in menu_options.items():
            ports = "/".join([highlight_ports(port, open_ports) for port in value["ports"]])
            print(f"[{key}] {value['name'].upper()}: Ports {ports}")
        print("[C] Type Commands")
        print("[0] Logout\n")

        choice = input("Enter your choice: ").strip().lower()

        # Handle global command input
        if choice == "c":
            global_command_handler()

        # Match the choice to a menu option
        elif choice in menu_options:
            menu_options[choice]["submenu"](target_ip, open_ports)  # Pass arguments directly

        # Handle exit options
        elif choice in ["0", "q", "exit", "quit"]:
            print("Logging out...")
            break

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
        
def global_command_handler():
    print("\nEntering Command Mode (type 'exit' to return to the menu)\n")
    while True:
        command = input(f"{Fore.YELLOW}Command > {Style.RESET_ALL}").strip()
        if command.lower() in ["exit", "quit"]:
            print("Exiting Command Mode...")
            break
        try:
            result = subprocess.run(command, shell=True, text=True, capture_output=True)
            if result.stderr:
                print(f"{Fore.RED}Error:\n{result.stderr}{Style.RESET_ALL}")
        except Exception as ex:
            print(f"{Fore.RED}An error occurred: {ex}{Style.RESET_ALL}")
