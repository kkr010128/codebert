N = int(input())
C = 10**9+7
A = list(map(int, input().split()))
ans = 0
for i in range(60):
    L = [(A[j] >> i) & 1 for j in range(N)]
    # print(L)
    a = L.count(0)
    b = L.count(1)
    ans += a*b*pow(2, i, C)
print(ans % C)
