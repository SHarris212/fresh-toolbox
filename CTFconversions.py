########## Possible: ##########
#         raw = the unencoded ASCII string (contains only printable characters that are not whitespace)
#         b64 = standard base64 encoding (see 'base64' unix command)
#         hex = hex (base 16) encoding (case insensitive)
#         dec = decimal (base 10) encoding
#         oct = octal (base 8) encoding
#         bin = binary (base 2) encoding (should consist of ASCII '0' and '1')


import base64
import socket

easy = {"hex" : 16 ,"oct" : 8,"dec" : 10,"bin" : 2}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("challenge.acictf.com",27205))
w.open("convDebug.txt","wa")

while True:
    r = s.recv(8192).split('\n')
    w.write(r)
    f = r[-4][:3]
    t = r[-4][-4:-1]
    enc = r[-3][:-1]
    if f in easy.keys() and t in easy.keys():
        unenc = int(enc, easy[f])
        if t == "bin"
           s.send((bin(unenc)[2:] + "\n").encoding('utf-8'))
        if t == "hex":
            s.send((hex(unenc)[2:] + "\n").encoding('utf-8'))
        if t == "dec":
            s.send((unenc + "\n").encoding('utf-8'))
        if t == "oct":
            s.send((oct(unenc)[2:] + "\n").encoding('utf-8'))
    elif f == "oct" and t == "raw":
        a = "" 
        for i in range(0,len(oct),3):
            a += chr(int(oct[i:i+3]))
        s.send((a + "\n").encoding('utf-8'))
    elif f == "raw" and t == "bin":
        a = ""
        for i in enc:
            a += bin(ord(i))[2:]
        s.send((a + "\n").encoding('utf-8'))
        

def quickConvert(f,t,enc):
    easy = {"hex" : 16 ,"oct" : 8,"dec" : 10,"bin" : 2}
    if f in easy.keys() and t in easy.keys():
        unenc = int(enc, easy[f])
        if t == "bin":
           return bin(unenc)[2:]
        if t == "hex":
            return hex(unenc)[2:]
        if t == "dec":
            return unenc
        if t == "oct":
            return oct(unenc)[2:]
    elif f == "oct" and t == "raw":
        a = "" 
        for i in range(0,len(oct),3):
            a += chr(int(oct[i:i+3]))
        return a
    elif f == "raw" and t == "bin":
        a = ""
        for i in enc:
            a += bin(ord(i))[2:]
        return a
    elif f == "raw" and t == "dec":
        a = ""
        for i in enc:
            a += str(ord(i))
        return a
        


#def bin2ascii(bin):
#    enc = hex(int(bin,2))[2:]
#    a = ""
#    for i in range(0,len(enc),2):
#        a += chr(int(enc[i:i+2],16))
#    return a
#
#def oct2ascii(oct):
#    a = ""
#    for i in range(0,len(oct),3):
#        a += chr(int(oct[i:i+3]))
#    return a
#
#def ascii2bin(ascii):

