import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    h1,m1,h2,m2,K = map(int, readline().split())

    wakeup = h1 * 60 + m1
    sleep = h2 * 60 + m2

    ans = sleep - K - wakeup
    print(ans)


if __name__ == "__main__":
    main()
