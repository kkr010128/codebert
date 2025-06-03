def resolve():
    import sys
    input = sys.stdin.readline
    # 整数 1 つ
    n = int(input())
    s = input()
    # 整数複数個
    # a, b = map(int, input().split())
    # 整数 N 個 (改行区切り)
    # N = [int(input()) for i in range(N)]
    # 整数 N 個 (スペース区切り)
    # N = list(map(int, input().split()))
    # 整数 (縦 H 横 W の行列)
    # A = [list(map(int, input().split())) for i in range(H)]

    cnt = 0
    for i in range(n-2):
        if s[i]+s[i+1]+s[i+2] == "ABC":
            cnt += 1

    print(cnt)
resolve()