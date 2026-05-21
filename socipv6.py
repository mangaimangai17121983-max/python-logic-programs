

import socket
 
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
 
s.connect(("::1", 80))
 
print("Connected to local IPv6 Apache server")

