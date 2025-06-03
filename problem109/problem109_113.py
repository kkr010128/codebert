import sys
input = sys.stdin.readline

def inp():
    return(int(input()))

def inpf():
    return(float(input()))


def inps():
    return str(input())



n = inp()
arr= []
cac = 0
cwa = 0
ctle = 0
cra = 0
for i in range(n):
    s = inps().rsplit()[0]
    if s=="AC": cac+=1
    elif s=="WA": cwa+=1
    elif s=="TLE": ctle+=1
    else: cra+=1
c = [cac, cwa, ctle, cra]
s = ["AC x ", "WA x ", "TLE x ", "RE x "]
for i in range(len(s)):
    print(s[i]+str(c[i]))