a, b = map(int, input().split())
if 2*b >= a:
    print(0)
elif 2*b < a:
    print(a-2*b)

