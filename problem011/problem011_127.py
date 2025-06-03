x, y = map(int, input().split())
a = max(x, y)
b = min(x, y)

while a%b != 0:
    temp = a
    a = b
    b = temp%b

print(b)