MOD = 10**9 + 7
MAX = int(2e5)


def div(a, b):
    return a * pow(b, MOD-2, MOD) % MOD


FACT = [1] * (MAX+1)
for i in range(1, MAX+1):
    FACT[i] = (i * FACT[i-1]) % MOD
INV = [1] * (MAX+1)
INV[MAX] = div(1, FACT[MAX])
for i in range(MAX, 0, -1):
    INV[i-1] = (INV[i] * i) % MOD


def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(min(n-1, k)+1):
        # iCn
        # (n-i-1)C(n-1)
        tmp = FACT[n] * INV[i] * INV[n-i] % MOD
        tmp = (tmp * FACT[n-1] * INV[n-i-1] * INV[i]) % MOD
        ans = (ans + tmp) % MOD
    print(ans)


if __name__ == "__main__":
    main()
