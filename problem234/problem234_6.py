n = int(input())
t = [[0 for j in range(10)] for i in range(10)]
for i in range(1,n+1):
    s = str(i)
    t[int(s[0])][int(s[-1])] += 1
ans = 0
for i in range(1,10):
    for j in range(1,10):
        ans += t[i][j]*t[j][i]
print(ans)