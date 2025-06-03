X = int(input())

x = X % 100
tmp = (x // 5) * 105
if x % 5 != 0:
    tmp += 100 + (x % 5)
if tmp > X:
    print(0)
else:
    print(1)
