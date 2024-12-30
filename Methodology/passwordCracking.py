def notes(target_ip, open_ports):
    title = "Notes"
    content = f"""
Password cracking Notes:
  - ./RSAcrack/RSAcrack -k doctor_rsa_key -w /usr/share/wordlists/seclists/Passwords/probable-v2-top12000.txt
"""
    run_command(title, content, target_ip, open_ports)