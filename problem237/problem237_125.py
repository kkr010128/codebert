INF = 1 << 60

n = int(input())
x = [0 for i in range(n)]
l = [0 for i in range(n)]
for i in range(n):
    x[i], l[i] = map(int, input().split())

itv = [[x[i] - l[i], x[i] + l[i]] for i in range(n)]
itv.sort(key=lambda x:x[1])
# print("itv =", itv)

ans = 0
t = -INF
for i in range(n):
    if t <= itv[i][0]:
        ans += 1
        t = itv[i][1]
print(ans)
