from netmiko import ConnectHandler
from getpass import getpass

host_list = [
    {
    "host" : "nxos1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type" : "cisco_nxos"
    },
    {
    "host" : "nxos2.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type" : "cisco_nxos"
    }
]


for host in host_list:
    connect = ConnectHandler(**host)
    print(connect.send_command("show version"))
    print(connect.find_prompt())
