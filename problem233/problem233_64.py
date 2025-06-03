import sys

def main():
    N = int(input())
    P = list(map(int, input().split()))
    min_so_far = sys.maxsize
    ans = 0
    for p in P:
        if p <= min_so_far:
            ans += 1
            min_so_far = p
    print(ans)


if __name__ == '__main__':
    main()
