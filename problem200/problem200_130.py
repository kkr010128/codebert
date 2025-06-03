def resolve():
    a, b, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    ans = min(a_list) + min(b_list)
    for _ in range(m):
        x, y, c = map(int, input().split())
        ans = min(ans, a_list[x-1]+b_list[y-1]-c)
    print(ans)
resolve()