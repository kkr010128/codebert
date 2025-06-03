def main():
    mod = 1000000007
    n = int(input())
    cnt = [0] * (n + 2)
    cnt[0] = 3
    res = 1
    for x in input().split():
        v = int(x)
        res *= cnt[v] - cnt[v + 1]
        res %= mod
        cnt[v + 1] += 1
    print(res)

main()

