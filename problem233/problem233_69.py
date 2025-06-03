N = int(input())
P = list(map(int, input().split()))

temp = P[0]
res = 1
for i in range(1,N):
    if P[i] <= temp:
        temp = P[i]
        res += 1
print(res)