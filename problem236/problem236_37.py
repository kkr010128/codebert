h = int(input())
w = int(input())
n = int(input())

if h >= w:
    larger = h
else:
    larger = w

if n % larger == 0:
    print(n // larger)
else:
    print(n // larger + 1)