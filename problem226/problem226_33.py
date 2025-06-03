x, y = map(int, input().split())
z = map(int, input().split())
if sum(z) >= x:
    print("Yes")
else:
    print("No")