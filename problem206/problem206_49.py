N = int(input())
a = 0
b = 0

if N % 2 == 0:
    a = N // 2
    print(a)
else:
    b = N // 2 + 1
    print(b)