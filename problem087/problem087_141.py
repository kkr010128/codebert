import math
n = sum([int(x) for x in str(input()).split()])

a, b = divmod(n, 9)

print("No" if b else "Yes")
