from netmiko import ConnectHandler

device={
    "device_type": "cisco_ios",
    "host": "devnetsandboxiosxec8k.cisco.com",
    "username":"gpaulatun",
    "password": "H-3S0_4ZqPqiZ"
}

with ConnectHandler(**device) as connection:
    result = connection.send_command(command_string= "show run | section ospf")
    print(result)