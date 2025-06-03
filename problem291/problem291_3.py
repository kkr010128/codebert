import sys
stdin=sys.stdin

ip=lambda: int(sp())

lp=lambda:list(map(int,stdin.readline().split()))
sp=lambda:stdin.readline().rstrip()

a,b=lp()

print(max(0,a-2*b))

