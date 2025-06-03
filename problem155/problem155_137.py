def main():
    import sys
    input = sys.stdin.buffer.readline
    N, M = (int(i) for i in input().split())
    H = [int(i) for i in input().split()]
    ans = [1]*N
    for _ in range(M):
        a, b = (int(i)-1 for i in input().split())
        if H[a] < H[b]:
            ans[a] = 0
        elif H[b] < H[a]:
            ans[b] = 0
        else:
            ans[a] = 0
            ans[b] = 0

    print(sum(ans))


if __name__ == '__main__':
    main()
