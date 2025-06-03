n, m = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
b = [int(input()) for j in range(m)]
ans = []

for a in A:
    multi_list = [x * y for (x, y) in zip(a, b)]  # 書き方:リストの要素同士の積
    arg = 0
    for k in multi_list:
        arg += k
    print(arg)
