from functools import reduce

print("Yes" if reduce(lambda a, b: (a+b)%9, map(int, input()), 0) == 0 else "No")
