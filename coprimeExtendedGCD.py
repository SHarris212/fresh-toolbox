#formula: p * u + q * v = 1

def extendedGCD(p,q):
    u = 1
    v = -1
    while(p * u + q * v != 1):
        if p * u + q * v == -1:
            u *= -1
            v *= -1
        if(abs(p*u) < abs(q*v)):
            u += 1
            print("U: {} || V: {} || Dist: {}".format(u,v,abs(p*u)-abs(q*v)))
        elif(abs(p*u) > abs(q*v)):
            v += -1
            print("U: {} || V: {} || Dist: {}".format(u,v,abs(q*v)-abs(p*u)))


extendedGCD(26513,32321)






