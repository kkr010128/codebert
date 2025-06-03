import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    mod = 10**9+7
    x, y = map(int, input().split())
    x2 = max(x, y)
    y2 = min(x, y)
    m = y2-(x2-y2)
    if m < 0 or m % 3 != 0:
        print(0)
    else:
        c = m // 3
        n = c*2+(x2-y2)
        bunshi = 1
        bunbo = 1
        for i in range(1, c+1):
            bunbo= bunbo*i % mod
            bunshi= bunshi*(n-i+1) % mod
    
        ans = bunshi * pow(bunbo,-1,mod)
        print(ans%mod)


if __name__ == '__main__':
    main()