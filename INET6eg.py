import socket
 
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
 
s.connect(("2405:201:e05c:805a:81b4:30e2:50a0:67dc", 80))
 
print("Connected to local IPv6 Apache server")
