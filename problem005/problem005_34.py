def GCD(a,b):
    while (a % b) != 0:
        a,b = b, a%b
    return b

def LCM(a,b):
    return a * b / GCD(a,b)

while True:
    try:
        a,b =map(int,raw_input().split())
        print GCD(a,b),LCM(a,b)
    except:
        break