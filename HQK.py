import socket
import time


def SendCommand(command,s):
    if len(bytes("{}\r\n".format(command),'utf-8')) > 2048:
        return b'Too long try again> '
    nsent = s.send(bytes("{}\r\n".format(command), 'utf-8'))
    print("Sent: {} bytes".format(nsent))
    time.sleep(1)
    r = s.recv(8192)
    return r


def main():
    banner = "==================================\n|              HQK               |\n==================================\n"
    print(banner)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("10.10.10.178",4386))
    r = s.recv(8192)
    #print(r.decode('utf-8'))
    while s:
        r = SendCommand(input(r.decode('utf-8')),s)
    s.close()

main()

exit()
