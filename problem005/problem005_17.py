def gcm(a, b):
    if a<b: a,b = b,a

    if (a%b ==0):
        return b
    else:
        return gcm(b, a%b)

def lcm(a, b):
    return a/gcm(a,b)*b

while True:
    try:
        a, b = map(int, raw_input().split())
    except:
        break
    print "%d %d" %(gcm(a,b), lcm(a,b))