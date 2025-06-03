def solve():
    n = int(input())
    s, t = input().split()
    ans = ""
    for x, y in zip(s, t):
        ans = ans + x + y
    print(ans)



solve()