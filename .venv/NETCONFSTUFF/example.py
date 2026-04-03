from ncclient import manager

my_device = manager.connect(
    host = "devnetsandboxiosxec8k.cisco.com",
    port = "830",
    timeout = 30,
    username = "gpaulatun",
    password = "c7_H_qtmOM03B",
    hostkey_verify=False
)

for capability in my_device.server_capabilities:
    print(capability)

my_device.close_session()