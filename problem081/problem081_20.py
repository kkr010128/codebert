ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(map(int, input().split()))

d, t, s = mi()
print("Yes" if d <= t*s else "No")