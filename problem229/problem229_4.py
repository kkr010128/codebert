h, n = map(int,input().split())
a = [0 for i in range(n)]
b = [0 for i in range(n)]
for i in range(n):
    ai ,bi = map(int,input().split())
    a[i] = ai
    b[i] = bi


mh = [0 for i in range(10003)]
for i in range(1,h+1):
    mb = 10**9
    for j in range(n):
        if mb > mh[i-a[j]] + b[j]:
            mb = mh[i-a[j]] + b[j]
    mh[i] = mb

print(mh[h])
