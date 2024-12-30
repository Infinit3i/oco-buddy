from colorama import Fore, Style
import subprocess


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
