from Modules.Imports.protocol_imports import *


def notes(target_ip, open_ports):
    title = "Notes"
    content = f"""
HTTP Notes:
  - sudo -l
    - gtfo bins
  - id
  - find / -uid <USER UUID> -type f -ls 2>/dev/null | grep -v '/proc*'
  - find / -name 'root.txt' -exec cat {{}} \\; 2>/dev/null
  - find / -perm -4000 -o -perm -2000 -ls 2>/dev/null
  - find /etc -perm -2
  - grep -Inri passw /etc/* 2>/dev/null
  - https://github.com/rebootuser/LinEnum
    - CVE-2019–13272
         openssl passwd
"""
    run_command(title, content, target_ip, open_ports)
