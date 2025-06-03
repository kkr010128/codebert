import functools
X = int(input())

@functools.lru_cache(maxsize=None)
def pow5(x):
    return x ** 5

@functools.lru_cache(maxsize=None)
def root5(x):
    i = 0
    while True:
        i5 = pow5(i)
        if x < i5:
            return None
        if i5 == x:
            return i
        i += 1

a = 0
while True:
    a5 = pow5(a)
    b = root5(a5 + X)
    if b is not None:
        print(-a, -b)
        break
    if a5 <= X:
        b = root5(X - a5)
        if b is not None:
            print(a, -b)
            break
    else:
        b = root5(a5 - X)
        if b is not None:
            print(a, b)
            break
    a += 1