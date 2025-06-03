import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline

INF = float('inf')


def main():
    s = map(int, input()[::-1])
    mod = 2019
    counts = [0] * mod
    counts[0] = 1
    t = 0
    x = 1
    for num in s:
        t = (t + num * x) % mod
        counts[t] += 1
        x = (x * 10) % mod
    ans = 0
    for count in counts:
        if count > 1:
            ans += count * (count - 1) // 2
    print(ans)


if __name__ == '__main__':
    main()
