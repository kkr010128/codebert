N = int(input())

def powmod(x, y):
    ret = 1
    for _ in range(1, y+1):
        ret = ret * x % (10**9+7)
    return ret
ans = powmod(10, N) - powmod(9, N)*2 + powmod(8, N)
print(ans % (10**9+7))