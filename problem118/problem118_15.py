

n = int(input())
l = [1]*(n+1)
l[0] = 0
ans = l[1]

for i in range(2,n+1):
    for j in range(i,n+1,i):
        l[j] += 1

    ans += (l[i]*i)




print(ans)
