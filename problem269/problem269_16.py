t = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [t[0]*a[0],t[1]*a[1]]
d = [t[0]*b[0],t[1]*b[1]]

if sum(c)==sum(d):
    print('infinity')
    exit()
elif c[0]==d[0]:
    print('infinity')
    exit()

if sum(d)>sum(c) and d[0]>c[0]:
    print(0)
    exit()
elif sum(c)>sum(d) and c[0]>d[0]:
    print(0)
    exit()
else:
    n = (c[0]-d[0])/(sum(d)-sum(c))
    if n==int(n):
        print(2*int(n))
    else:
        print(2*int(n)+1)
