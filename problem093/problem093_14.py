import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    p = tuple(map(int, input().split()))
    c = tuple(map(int, input().split()))
    ans = -10**18
    for i in range(n):
        start, count = i, 1
        val = c[start]
        while p[start]-1 != i:
            start = p[start]-1
            count += 1
            val += c[start]
        start = i
        if val > 0:
            a = (k//count-1)*val
            ans = max(a, ans)
            num = count + k % count
        else:
            a = 0
            num = min(k, count)
        for _ in range(num):
            a += c[start]
            start = p[start] - 1
            ans = max(a, ans)
    print(ans)


if __name__ == '__main__':
    main()