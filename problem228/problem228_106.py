def func(h):
    if h == 1:
        h = 0
        return 1
    else:
        return 1 + 2 * func(h//2)

h = int(input())
print(func(h))