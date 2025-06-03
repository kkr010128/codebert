a, b = map(int, input().split())
if a > 0 and a < 10:
    if b > 0 and b < 10:
        print(a * b)
    else:
        print(-1)
else:
    print(-1)
