# Great for small number, havent tested the limit, but I'd say anything past billions or trillions is bad juju
def findDevisors(num):
    dev = []
    for i in range(1,round(num/2)):
        if num % i == 0:
            if i in dev or round(num/i) in dev:
                return dev
            else:
                dev.append(i)
                dev.append(round(num/i))
    return dev

# uses my above function to find devisors and then returns the greatest common devisor
def findGCD(num1,num2):
    cd = []
    nd1 = findDevisors(num1)
    nd2 = findDevisors(num2)
    for d in nd1:
        if d in nd2: cd.append(d)
    for d in nd2:
        if d in nd1 and d not in cd: cd.append(d)
    cd.sort()
    return cd[-1]


# formula: p * u + q * v = 1
# I'm sure theres a better way to do this, but I wanted it to work 
# with more ints than just coprime integers
def extendedGCD(p,q):
    GCD = findGCD(p,q)
    u = 1
    v = -1
    while(p * u + q * v != GCD):
        if p * u + q * v == GCD * -1:
            u *= -1
            v *= -1
        if(abs(p*u) < abs(q*v)):
            u += 1
        elif(abs(p*u) > abs(q*v)):
            v += -1
    print("GCD: {} || U: {} || V: {}".format(GCD,u,v))


#Reads PEM encoded RSA key file and returns the key
def readRSAKey(file):
    from Crypto.PublicKey import RSA
    f = open(file,'r')
    key = RSA.importKey(f.read())
    return key

# Given a hex string (just flat HEX ie "aabbccddee112233", and a 
# flat hex key, ie "1e4c" XOR and return the string

def stringXORdecode(origHex,key):
    a = ""
    s = 0
    for b in range(0,len(origHex),2):
        if s >= len(key):
            s = 0
        a += chr(int(origHex[b:b+2],16) ^ int(key[s:s+2],16))
        s += 2
    return a


# Brute forces XOR decoding and prints it
# 
# I plan on adding a write to file function 
# that will allow you to tell it to write to a file
#
# Eventually I also want it to remove non ascii printable 
# characters, but haven't figured out how to do that without 
# significantly reducing the XOR speed

def bruteXORdecode(origHex,origKey):
    for i in range(0,256):
        key = origKey
        key = key.replace("__", hex(i)[2:].zfill(2),1)
        if "__" in key:
            bruteXORdecode(origHex,key)
        else:
            result = stringXORdecode(origHex,key)
            print("Key: {} Result: {}\n".format(key,result))
            

#flag = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
# key = '__'

