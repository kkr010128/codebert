import sys
n,k=map(int,input().split())
h=list(map(int,input().split()))

h.sort(reverse=True)

if len(h)<=k:
    print('0')
    sys.exit()
else:
    del h[0:k]

a=sum(h)

print(a)
