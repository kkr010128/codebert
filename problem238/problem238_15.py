n, k, s = map(int,input().split())

t1 = [str(s)] * k

if s != 10**9:
    t2 = [str(s+1)] * (n-k)
else:
    t2 = [str(1)] * (n-k)

print(*(t1+t2))