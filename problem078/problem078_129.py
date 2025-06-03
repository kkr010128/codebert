N = int(input())
# x の y 乗を d で割った余りを求める
def powmod(x, y, d):
    ret = 1
    for _ in range(1, y+1):
        ret = ret * x % d
    return ret
ans = powmod(10, N, 10**9+7) - powmod(9, N, 10**9+7)*2 + powmod(8, N, 10**9+7)

print(ans % (10**9+7))


