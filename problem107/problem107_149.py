n = int(input())
s2 = input()

l = [int(i) for i in s2]
p = sum(l)
s10 = int(s2,2)
if p == 1:
    ans1 = s10%(p+1)
    l1 = [0]*(n+1)
    l1[0] = 1
    for i in range(1,n+1):
        l1[i] = (l1[i-1]*2)%(p+1)
    for i in range(n):
        if l[i]:
            print(0)
        else:
            first = (ans1 + l1[n-i-1])%(p+1)
            ans = 1
            while first:
                mod = 0
                for j in range(len(bin(first))-2):
                    mod += first >> j & 1
                first %= mod
                ans += 1
            print(ans)
    quit()
if p == 0:
    for i in range(n):
        print(1)
    quit()

ans1 = s10%(p+1)
ans2 = s10%(p-1)
l1 = [0]*(n+1)
l2 = [0]*(n+1)
l1[0] = 1
l2[0] = 1
for i in range(1,n+1):
    l1[i] = (l1[i-1]*2)%(p+1)
    l2[i] = (l2[i-1]*2)%(p-1)
first = []
for i in range(n):
    if l[i]:
        first.append((ans2-l2[n-i-1])%(p-1))
    else:
        first.append((ans1+l1[n-i-1])%(p+1))


for i in range(n):
    if first[i] == 0:
        print(1)
        continue
    x = first[i]
    ans = 1
    while x:
        mod = 0
        for j in range(len(bin(x))-2):
            mod += x >> j & 1
        x = x%mod
        ans += 1
    print(ans)