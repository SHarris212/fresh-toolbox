def findDev(num):
    dev = []
    for i in range(1,round(num/2)):
        if num % i == 0:
            if i in dev or round(num/i) in dev:
                return dev
            else:
                dev.append(i)
                dev.append(round(num/i))
    return dev


def findGCD(num1,num2):
    cd = []
    nd1 = findDev(num1)
    nd2 = findDev(num2)
    for d in nd1:
        if d in nd2: cd.append(d)
    for d in nd2:
        if d in nd1 and d not in cd: cd.append(d)
    cd.sort()
    return cd[-1]

def findUV(num1,num2)
    igcd = findGCD(num1,num2)
    u = 1
    v = 1
    while(num1*u + num2*v != igcd)
