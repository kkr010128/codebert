n = int(input())
if n == 2 * int(n / 2):
    p = 1 / 2
else:
    p = (n + 1) / (2 * n)
print(p)