import paramiko
import time
import socket


def send_command(
        ip,
        username,
        password,
        enable,
        commands,
        max_bytes=60000,
        short_pause=1,
        long_pause=3,
):
    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cl.connect(
        hostname=ip,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
    )
    with cl.invoke_shell() as ssh:
        ssh.send(bytes("enable\n", encoding="utf-8"))
        ssh.send(bytes(f"{enable}\n", encoding="utf-8"))
        time.sleep(short_pause)
        ssh.send(bytes("terminal length 0\n", encoding="utf-8"))
        time.sleep(short_pause)
        ssh.recv(max_bytes)

        result = {}
        for command in commands:
            ssh.send(bytes(f"{command}\n", encoding="utf-8"))
            ssh.settimeout(long_pause)

            output = ""
            while True:
                try:
                    part = ssh.recv(max_bytes).decode("utf-8")
                    output += part
                    time.sleep(0.5)
                except socket.timeout:
                    break

            result[command] = output

        return result
