import socket
import sys
from datetime import datetime


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Usage: {} <ip>".format(sys.argv[0]))
    sys.exit(1)
    
print("{0}\nScanning target: {1}\nTime started: {2}\n{0}".format("-"*50,target,datetime.now()))
try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} - OPEN".format(port))
        s.close()

except KeyboardInterrupt: 
    print("\nCtrl-C, exiting.")
    sys.exit(1)

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit(2)

except socket.error:
    print("Unable to connect to server")
    sys.exit(3)



