x, y = map(int, input().split())
if x <= y:
    print(1)
elif x % y == 0:
    print(x//y)
else:
    print(x//y+1)
