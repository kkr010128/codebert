A,B = map(int, input().split())

a = A - B * 2

if a <= 0:
    print("0")
else:
    print(a)