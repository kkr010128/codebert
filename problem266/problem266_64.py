x = int(input())
q, r = divmod(x, 100)
if 0 <= r <= 5*q:
    print(1)
else:
    print(0)
