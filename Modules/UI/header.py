from colorama import Fore, Style  # For text color formatting
from Modules.UI.clear_screen import clear_screen  # Clears the terminal screen
from Modules.UI.center_text import center_text  # Centers text on the screen
from Modules.UI.random_tip import get_random_tip_with_color  # Provides a random tip with color
from Assets.ascii_text_prompts import ascii_art  # ASCII art banner
from Modules.Login.scan import BACKGROUND_TASK  # Background tasks tracking


def header(target_ip, open_ports):
    clear_screen()
    print(center_text(ascii_art))  # Display the full ASCII art banner
    print(center_text(get_random_tip_with_color()) + "\n")
    print(center_text(f"Target IP: {target_ip}\n"))
    if open_ports:
        print(center_text(f"Open Ports: {Fore.GREEN}{', '.join(map(str, open_ports))}{Style.RESET_ALL}\n"))
    else:
        print(center_text("Open Ports: None\n"))
    if BACKGROUND_TASK:
        print(center_text("Background Commands:"))
        for task in BACKGROUND_TASK:
            print(center_text(f"- {Fore.YELLOW}{task}{Style.RESET_ALL}"))
        print()  # Add spacing
    else:
        print(center_text("Background Commands: None\n"))