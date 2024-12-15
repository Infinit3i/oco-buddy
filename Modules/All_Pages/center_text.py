import os  # To use os.get_terminal_size()

def center_text(text):
    terminal_width = os.get_terminal_size().columns
    centered_lines = []
    for line in text.splitlines():
        centered_lines.append(line.center(terminal_width))
    return "\n".join(centered_lines)