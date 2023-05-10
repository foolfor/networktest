# A CLI based pytest network testing tool



Example:

```python
from ssh_test import ssh_cmd
from ssh_test import ssh_contain

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


def test_version():
    result = ssh_cmd.send_command(host, username, password, secret, commands)
    value = result[commands[0]]
    assert ssh_contain.cmd_contain(value, 'UUID')
```

