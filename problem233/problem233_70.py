n = int(input())
p = list(map(int,input().split()))

minp =[p[0]]

for i in range(1,n):
    minp.append(min(minp[i-1],p[i]))


cnt = 0
for i in range(n):
    if minp[i] == p[i]:
        cnt += 1
print(cnt)