def judge99(x):
    if x <= 9:
        return True
    else:
        return False

a, b = map(int,input().split())

if judge99(a) and judge99(b):
    print(a*b)
else:
    print(-1)
