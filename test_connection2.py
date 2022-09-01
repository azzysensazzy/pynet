from netmiko import ConnectHandler
from getpass import getpass

host_list = [
    {
    "host" : "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type" : "cisco_xe"
    }
]

command_output = ""

for host in host_list:
    connect = ConnectHandler(**host)

command_output=connect.send_command("show version")

with open("cisco3.lasthop.io.txt", "w") as file:
    file.write(command_output)
