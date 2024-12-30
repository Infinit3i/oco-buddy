import os
import platform


def clear_screen():
    # Check the system platform and use the appropriate command
    if platform.system().lower() == "windows":
        os.system('cls')  # Windows command to clear the screen
    else:
        os.system('clear')  # Unix-based (Linux/macOS) command to clear the screen