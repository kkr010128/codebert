if __name__ == '__main__':
    n = int(input())
    a = list(map(lambda x: int(x) + 1, input().split()))
    counts = [0] * (n + 1)
    counts[0] = 3
    ans = 1
    for i in range(n):
        ans *= counts[a[i] - 1]
        ans %= (10 ** 9 + 7)
        counts[a[i] - 1] -= 1
        counts[a[i]] += 1
    print(ans)
