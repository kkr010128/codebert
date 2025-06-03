import sys

readline = sys.stdin.readline

def main():
    A, B, M = map(int, readline().split())
    a = list(map(int, readline().split()))
    b = list(map(int, readline().split()))
    ans = min(a) + min(b)
    for _ in range(M):
        x, y, c = map(int, readline().split())
        ans = min(ans, a[x-1] + b[y-1] - c)
    print(ans)


if __name__ == "__main__":
    main()
