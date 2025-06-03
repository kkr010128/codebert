def solve():
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    if sum(s) >= n:
        print("Yes")
    else:
        print("No")

solve()