import importlib
import threading
import logging
import inspect
from Protocols.menu import MENU_OPTIONS

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def automatic_enumeration(target_ip, open_ports):
    logging.info("=== Automatic Enumeration Started ===")

    for protocol, details in MENU_OPTIONS.items():
        protocol_ports = details["ports"]
        detected_ports = [port for port in open_ports if port in protocol_ports]

        if detected_ports:
            logging.info(f"[Auto] Detected Protocol: {details['name'].upper()} on Ports: {', '.join(detected_ports)}")
            try:
                module = importlib.import_module(f"Protocols.{details['module']}")
                logging.info(f"[Auto] Enumerating {details['name'].upper()}...")
                execute_protocol_functions(module, target_ip, detected_ports)
            except ModuleNotFoundError:
                logging.error(f"[Auto] Error: Protocol module '{details['module']}' not found.")
            except Exception as ex:
                logging.exception(f"[Auto] An unexpected error occurred: {ex}")


def execute_protocol_functions(module, target_ip, detected_ports):
    """
    Execute all functions in the imported module in the order they are defined.
    """
    source = inspect.getsource(module)
    lines = source.splitlines()
    actions = []

    for line in lines:
        if line.strip().startswith("def "):  # Identify function definitions
            func_name = line.strip().split(" ")[1].split("(")[0]
            func = getattr(module, func_name, None)
            if func and inspect.isfunction(func):
                actions.append((func_name, func))

    # Execute each function in order
    for func_name, func in actions:
        logging.info(f"[Auto] Running {func_name.replace('_', ' ').title()}...")
        try:
            func(target_ip, detected_ports)
        except Exception as ex:
            logging.exception(f"[Auto] An error occurred while running {func_name}: {ex}")


def start_automatic_enumeration(target_ip, open_ports):
    """
    Starts automatic enumeration in a background thread.
    """
    thread = threading.Thread(target=automatic_enumeration, args=(target_ip, open_ports), daemon=True)
    thread.start()
