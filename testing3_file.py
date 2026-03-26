from netmiko import ConnectHandler

device={
    "device_type": "cisco_ios",
    "host": "devnetsandboxiosxec8k.cisco.com",
    "username":"gpaulatun",
    "password": "H-3S0_4ZqPqiZ"
}

configs=[
    "router ospf 1","router-id 1.1.1.1", "network 10.0.0.0 0.0.0.255 area 0"
]

with ConnectHandler(**device) as connection:
    result = connection.send_config_from_file(config_file="config.cfg")
    print(result)