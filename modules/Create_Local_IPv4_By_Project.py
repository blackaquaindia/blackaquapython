import random
# Perform actions for each line here
Gateway = random.randint(2, 255)
Static = random.randint(2, 255)
IPv4File = f"C:/BlackAquaPython/IPv4/{project}.bat"
with open(IPv4File, "w") as bat_file:
    bat_file.write(f"netsh interface ipv4 set address name=\"Ethernet 2\" static 192.168.{Gateway}.{Static} 255.255.255.0 192.168.{Gateway}.1")

