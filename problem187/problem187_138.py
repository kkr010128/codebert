def main():
    import sys
    readline = sys.stdin.buffer.readline

    n, x, y = map(int, readline().split())

    l = [0] * (n-1)
    for i in range(1, n):
        for j in range(i+1, n+1):
            s = min(j-i, abs(x-i)+abs(j-y)+1)
            l[s-1] += 1
    for i in l:
        print(i)

if __name__ == "__main__":
    main()