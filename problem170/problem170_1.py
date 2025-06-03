def solve(n, k):
    ans = 0
    mod = int(1e9 + 7)
    for i in range(k, n + 2):
        lb = (i - 1) * i // 2
        ub = (n + n - i + 1) * i // 2
        ans += ub - lb + 1
        ans %= mod
        # print(ub-lb+1, ub, lb, i)
    return ans


def main():
    # print(solve(3, 2))
    # print(solve(200000, 200001))
    # print(solve(141421, 35623))
    print(solve(*[int(v) for v in input().split()]))


if __name__ == '__main__':
    main()
