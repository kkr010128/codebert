n,k = map(int,input().split())
P = list(map(int,input().split()))

s=0
for i in range(k):
    s += P[i]

ms=s
for i in range(len(P)-k):
    s +=(P[i+k]-P[i])
    if s>ms :
        ms=s

print( (ms+k)/2)


