# A CLI based pytest network testing tool

## Example

```python
from ssh_test import ssh_cmd, ssh_contain

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

```

## Do not test the same command in one case

The `ssh_cmd.send_command` will return a dict. So the elements of  the `commands` list will be the keys for the `result` dict. So that, the elements of the `commands` list cannot be duplicated.

The following example is incorrect.

```python
commands = ["sys", "int g 1/0/0", "exit", "exit"]
```

Because of the keys in the dict are unique. So the value of  `commands[2]` will be covered by the value of `commands[3]` that is the final value of  `result["exit"]`.  

The following example is correct.

```python
commands = ["sys", "int g 1/0/0", "quit", "exit"]
```

If you want to test the `exit` function in the same case, you must find another command like `quit`. If there are no two different command to distinguish between, I suggest you split a test case into two.

## Using `secret` to distinguish different vendors

The `secret` is the password of the enable mode by Cisco type default. If you want to test HUAWEI or H3C type, you must define the value of `secret` as in the following example. Their equipments have no enable mode.

```python
# Change to HUAWEI or H3C Type
secret = "H"
```

## Send `Ctrl-C` in `commands`.

The `^C` refers to `Ctrl-C`. If you want to send `Ctrl-C`, the following example can be useful.

```python
commands = ["test", "^C"]
```
