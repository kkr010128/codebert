N = int(input())
A = list(map(int,input().split()))
mod = 10**9+7
ans = 0

for bit in range(60):
    m = 1 << bit
    # bit桁目のbitが立っている時の数
    c = sum(a&m for a in A) >> bit
    # bit桁目の1の合計
    ans += (c*(N-c))<<bit
    # 繰り上がりのない足し算
    ans %= mod
print(ans)