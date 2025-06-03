
def resolve():
    MOD = 10 ** 9 + 7
    N, K = map(int, input().split())
    ans = 0
    for k in range(K, N + 2):
        min_num = k * (k - 1) // 2
        max_num = k * (N * 2 - k + 1) // 2
        add = max_num - min_num + 1
        ans = (ans + add) % MOD
    print(ans)

if __name__ == "__main__":
    resolve()