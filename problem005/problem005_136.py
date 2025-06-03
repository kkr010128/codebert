import sys
def gcm(a, b):
    if a<b: a,b=b,a
    if (a%b==0):
        return b
    else:
        return gcm(b,a%b)

for s in sys.stdin:
    a,b=map(int,s.split())
    c=gcm(a,b)
    print "%d %d" %(c,a/c*b)