mod = 1000000007

n = int(input())
A = list(map(int,input().split()))

d = {-1:3}
ans = 1
for a in A:
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1
    if a-1 not in d:
        print(0)
        exit()
    ans = ans*d[a-1]%mod
    d[a-1] -= 1

#print(d)
print(ans)