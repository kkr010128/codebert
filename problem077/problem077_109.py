a, b, c, d= map(int, input().split())

if a <= 0 and b <= 0 and c<= 0 and d<= 0:
    print(a * c)
elif a <= 0 and b<= 0 and c > 0 and d > 0:
    print(b * c)
elif a > 0 and b > 0 and c <= 0 and d <= 0:
    print(a * d)
elif a * c >= b * d:
    print(a * c)
elif a * c < b * d:
    print(b * d)

