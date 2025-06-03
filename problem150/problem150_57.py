n, k  = map(int, input().split())
an = list(map(int, input().split()))
bn = [-1]*(n+1)

now=1
bn[1]=0
for i in range(1, k+1):
 #   print(bn)
    now = an[now-1]
    if bn[now] >0:
        rp =i-bn[now]
        p= (k-i)%rp
        for j in range(p):
            now = an[now-1]
        print(now)
        exit(0)
    bn[now]=i
print(now)