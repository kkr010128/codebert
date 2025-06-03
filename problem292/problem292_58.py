def main():
    import sys
    readline = sys.stdin.buffer.readline

    n = int(readline())
    d = list(map(int, readline().split()))

    e = sum(d)
    ans = 0
    for i in d:
        e -= i
        ans += i*e
    print(ans)

if __name__ == '__main__':
    main()