a, b, c, d = list(map(int, input().split(" ")))
if a <= b and c <= d:
    print(max(a*c, a*d, b*c, b*d))