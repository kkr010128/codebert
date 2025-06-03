a, b = map(str, input().split())
c, d = map(int, input().split())
e = str(input())
if e==a:
    print(c-1, d)
elif e==b:
    print(c, d-1)
