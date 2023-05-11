from ssh_test import ssh_cmd, ssh_contain
from pprint import pprint

# the management ip address of DUT
host = "192.168.0.1"
# username of the ssh connect
username = "cisco"
# password of the ssh connect
password = "cisco"
# password of the enable mode
secret = "cisco"
# list the commands, example:
# commands = ["show version", "show clock"]
commands = ["show version", ]

result = ssh_cmd.send_command(host, username, password, commands, secret)
value = result[commands[0]]


def test_version():
    assert ssh_contain.cmd_contain(value, 'UUID')


if __name__ == "__main__":
    print(value)
    print("======================")
    pprint(result, width=20)
