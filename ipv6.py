import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[+] Socket successfully created!")


SOCKET IPV6 COMMUNICATION

import socket
 
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
 
s.connect(("::1", 80))
 
print("Connected to local IPv6 Apache server")

