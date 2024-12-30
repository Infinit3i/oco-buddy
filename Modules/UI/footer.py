from colorama import Fore, Style
from Modules.Utils.common import global_command_handler


def display_footer(actions, target_ip, open_ports):
    print("[C] Type Commands")
    print("[0] Back to Main Menu\n")

    # Get user choice for submenu
    sub_choice = input("Select an option: ").strip().lower()
    if sub_choice == "0":
        return False  # Exit the menu
    elif sub_choice == "c":
        global_command_handler()
    elif sub_choice.isdigit() and 1 <= int(sub_choice) <= len(actions):
        selected_func = list(actions.values())[int(sub_choice) - 1]
        selected_func(target_ip, open_ports)
        return True  # Stay in the menu
    else:
        print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
        return True  # Stay in the menu
