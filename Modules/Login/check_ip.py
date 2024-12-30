from Modules.UI.clear_screen import clear_screen
from Assets.ascii_text_prompts import full_ascii_art, infinitei
from Modules.UI.center_text import center_text

# Declare TARGET_IP
TARGET_IP = None


def is_valid_ip(ip):
    try:
        segments = ip.split(".")
        if len(segments) != 4:  # Ensure it has exactly 4 segments
            return False
        for segment in segments:
            if not segment.isdigit() or not (0 <= int(segment) <= 255):  # Check if it's numeric and in range
                return False
        return True
    except Exception:
        return False


def get_target_ip():
    global TARGET_IP
    while True:
        clear_screen()
        print(center_text(full_ascii_art))  # Display the full ASCII art banner
        print(center_text(infinitei))  # Display the full ASCII art banner
        input_ip = input("Enter target IP: ").strip()
        if is_valid_ip(input_ip):
            TARGET_IP = input_ip
            print(f"Valid IP: {TARGET_IP}")
            return TARGET_IP  # Explicitly return the target IP
        else:
            print("Invalid IP. Please try again.")


def retrieve_target_ip():
    return TARGET_IP


def get_box_name():
    while True:
        clear_screen()
        print(center_text(full_ascii_art))  # Display the full ASCII art banner
        print(center_text(infinitei))  # Display the full ASCII art banner
        box_name = input("Enter the name of the box: ").strip()
        if box_name:
            return box_name
        print("Box name cannot be empty. Please try again.")