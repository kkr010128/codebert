N,K = map(int,input().split())
p = list(map(int,input().split()))

l = []
for i in p:
    l.append((1/2*i*(i+1))/i)

s = [0]*len(l)
s[0] = l[0]
for i in range(1,len(l)):
    s[i] = s[i-1]+l[i]

ans = 0
for i in range(K,len(s)):
    ans = max(ans,s[i]-s[i-K])

if N == K:
    print(max(s))
    exit()

print(ans)