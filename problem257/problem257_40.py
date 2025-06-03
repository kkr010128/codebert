def main():
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    target = 1
    for i in A:
        if i == target:
            target += 1
    
    if target == 1:
        print(-1)
        return

    print(N - target + 1)


main()