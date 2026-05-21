import socket
 
s = socket.socket()
 
s.settimeout(5)
 
status = s.connect_ex(("127.0.0.1", 80))
 
if status == 0:
	print("[+] Port 80 is OPEN")
 
else:
    print("Port 80 is closed")
    print(f"Error code:{status}")


    if status==10061:
        print("Reason: connection refused")

    elif status==10060:
        print("Reason:connection timed out")

    elif status==10035:
        
        print("Reason:Operation would block")

    else:
        print("Reason:unknown")
    
 
 
 
