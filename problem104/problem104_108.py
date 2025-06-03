def func(num, div):
    return num // div


l, r, d = map(int, input().split())

print(func(r, d) - func(l - 1, d))

