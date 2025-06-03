from collections import defaultdict
def main():
    n, x, y = map(int, input().split())
    ans = defaultdict(int)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            l = min(abs(i - j), abs(i - x) + abs(y - j) + 1, abs(i - y) + abs(x - j) + 1)
            ans[l] += 1
    [print(ans[i]) for i in range(1, n)]

if __name__ == '__main__':
    main()
