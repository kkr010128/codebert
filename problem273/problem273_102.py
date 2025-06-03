n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = a[i] % k

if k == 1:
    print(0)
    exit()

ruiseki = [0]
for i in range(n):
    ruiseki.append((a[i]+ruiseki[-1])%k)

mini = 0
dic = {}
ans = 0
for j in range(1, n+1):
    if j-k+1 > mini:
        dic[(ruiseki[mini]-mini)%k] -= 1
        mini += 1
    if (ruiseki[j-1]-(j-1))%k in dic:
        dic[(ruiseki[j-1]-(j-1))%k] += 1
    else:
        dic[(ruiseki[j-1]-(j-1))%k] = 1
    if (ruiseki[j]-j)%k in dic:
        ans += dic[(ruiseki[j]-j)%k]
print(ans)