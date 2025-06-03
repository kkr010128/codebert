import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def main():
    n, p = map(int, input().split())
    s = list(input())
    if 10 % p == 0:
        ans = 0
        for i in range(n):
            if (ord(s[i])-ord('0')) % p == 0:
                ans += i+1
        print(ans)
        return

    d = [0] * (n+1)
    ten = 1
    for i in reversed(range(n)):
        a = (ord(s[i])-ord('0')) * ten % p
        d[i] = (d[i+1]+a) % p
        ten *= 10
        ten %= p

    cnt = [0] * p
    ans = 0
    for i in reversed(range(n+1)):
        ans += cnt[d[i]]
        cnt[d[i]] += 1
    print(ans)


main()
