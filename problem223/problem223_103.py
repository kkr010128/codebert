n,k = map(int,input().split())
li = list(map(int,input().split()))

if n==k:
    ans = 0
    for i in li:
        ans += i*0.5+0.5
    print(ans)
    exit()

K = sum(li[:k])
ans = K
t = 0
for i in range(n-k):
    K += li[i+k] - li[i]
    if K > ans:
        ans = K
        t = i
ans = 0
for i in range(k):
    ans += li[t+i+1]*0.5 + 0.5
print(ans)