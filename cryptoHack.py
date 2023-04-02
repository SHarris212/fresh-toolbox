import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("socket.cryptohack.org",13377))
for i in range(0,105):
    t = s.recv(8192)
    print(t)
    t = json.loads(t.decode('utf-8'))
    if t["type"] == "hex":
        answer = bytearray.fromhex(t["encoded"]).decode('utf-8')
    elif t["type"] == "base64":
        answer = base64.b64decode(t["encoded"]).decode('utf-8')
    elif t["type"] == "rot13":
        answer = codecs.decode(t["encoded"], 'rot_13')
    elif t["type"] == "bigint":
        answer = bytearray.fromhex(t["encoded"][2:]).decode('utf-8')
    elif t["type"] == "ascii":
        answer = "".join([chr(b) for b in t["encoded"]])
    response = "{{\"decoded\": \"{}\"}}".format(answer)
    print(answer)
    s.send(response.encode('utf-8'))


''.join([chr(int(bin(ord(l) ^ 13),2)) for l in "label"])
for i in range(1,256):
    a = ''.join([chr(int(bin(l ^ i),2)) for l in bytearray.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")])
    if "crypto" in a:
        print(a)
