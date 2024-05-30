import math

def solution(numer1, denom1, numer2, denom2):
    numer3 = numer1 * denom2 + numer2 * denom1 # 분자
    denom3 = denom1 * denom2 # 분모
    
    #print(math.gcd(numer3, denom3))
    #print(type(math.gcd(numer3, denom3)))
    
    numer4 = numer3 / math.gcd(numer3, denom3)
    denom4 = denom3 / math.gcd(numer3, denom3)
    return [numer4, denom4]
"""
def euclidian(a, b):
    mod = 1
    gcd = 0
    while mod != 0:
        mod = (a // b) % (ab
        #mod = b
        gcd = b
        print(mod)
    return gcd
        
def solution(numer1, denom1, numer2, denom2):
    numer3 = numer1 * denom2 + numer2 * denom1
    denom3 = denom1 * denom2
    
    x = numer3
    y = denom3
    
    if numer3 > denom3:
        gcd = euclidian(numer3, denom3)
    else:
        gcd = euclidian(denom3, numer3)
        
    return [x / gcd, y / gcd]
"""