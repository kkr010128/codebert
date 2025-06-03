import sys
n,a,b = map(int,input().split())
if a == 0:
    print(0)
    sys.exit()

if b == 0:
    print(n)
    sys.exit()

if n%(a+b) <= a:
    print(n//(a+b)*a + n%(a+b))
else:
    print(n//(a+b)*a + a)
