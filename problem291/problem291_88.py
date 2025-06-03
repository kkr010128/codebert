A, B = (int(x) for x in input().split())

ans = A - (2 * B)
if ans > 0:
    print(ans)
else:
    print(0)