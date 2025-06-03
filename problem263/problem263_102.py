def main():
    n = int(input())
    A = list(map(int, input().split()))
    M = max(A)
    dig = len(bin(M)) - 2
    MOD = 10 ** 9 + 7
    ans = 0
    d = {i: 0 for i in range(dig)}
    for a in A:
        a = bin(a)[2:]
        for i in range(len(a)):
            if a[-(i+1)] == '1':
                d[i] += 1
    for i in range(dig):
        ans += d[i] * (n - d[i]) * pow(2, i, MOD)
        ans %= MOD
    print(ans)
main()
