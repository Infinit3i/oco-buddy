import sys  # For exiting the program
from Modules.All_Pages.clear_screen import clear_screen
from Modules.All_Pages.wrappers import header  # Import the header function

def build_submenu(menu_title, target_ip, actions, open_ports):
    # Initialize a dictionary to track the status of actions
    action_status = {key: False for key in actions}  # False means not completed

    while True:
        clear_screen()
        header(target_ip, open_ports)  # Call the header with the target_ip and open_ports
        print("=====================================")
        print(f"         {menu_title} Menu        ")
        print("=====================================\n")

        # Display menu options with status
        for key, action in actions.items():
            status = "✔️ " if action_status[key] else "❌"  # Check mark if completed, cross otherwise
            print(f"[{key}] {status} {action['description']}")
        print("[0] Return to Main Menu")
        print("[q] EXIT\n")

        # Get user choice
        choice = input("Enter your choice: ").strip().lower()

        # Handle menu choices
        if choice in actions:
            # Call the associated function with target_ip and update status
            actions[choice]["function"](target_ip, open_ports)
            action_status[choice] = True  # Mark the action as completed
        elif choice == "0":
            print("Returning to main menu...")
            break
        elif choice in ["q", "exit", "quit"]:
            print("Logging out...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")