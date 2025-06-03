
n = int(input())
a = [int(x) for x in input().split()]

deta = [0] * (n+1)

for i in a:
    deta[i] += 1

ans = [0] * (n+1)

for j in range(n+1):
    if deta[j] > 1:
        ans[j] = deta[j]*(deta[j]-1)/2
    else :
        ans[j] = 0

add = sum(ans)

for k in a:
    print(int(add - deta[k]*(deta[k]-1)/2 + (deta[k]-1)*(deta[k]-2)/2))
