a, b, n = map(int, input().split())
x = b-1 if n >= b else n
print(a*x//b)