import sys
r,g,b=map(int,input().split())
k=int(input())

for i in range(k+1):
    if r<g<b:
        print("Yes")
        sys.exit()
    else:
        if r<=b<=g:
            b*=2
        elif b<=r<=g:
            b*=2
        elif b<=g<=r:
            b*=2
        elif g<=r<=b:
            g*=2
        elif g<=b<=r:
            b*=2
print("No")

