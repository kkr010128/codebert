import sys
x,n = map(int,input().split())
p = list(map(int,input().split()))

if p.count(x) == 0:
    print(x)
else:
    for i in range(1,110):
        if p.count(x-i) == 0:
            print(x-i)
            sys.exit()
        elif p.count(x+i) == 0:
            print(x+i)
            sys.exit()
