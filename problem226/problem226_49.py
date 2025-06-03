a, b = map(int, input().split())
c = list(map(int, input().split()[:b]))
d = sum(c)
if d >= a:
    print("Yes")
else:
    print("No")