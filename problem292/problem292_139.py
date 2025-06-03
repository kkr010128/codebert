N = int(input())
d = list(map(int,input().split()))
amount = 0
b = [0] * N
for i in range(N):
    b[i] = amount
    amount += d[N-1-i]


ans = 0
for i in range(N):
    ans += d[i]*b[N-1-i]
print(ans)