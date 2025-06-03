n = int(input())
y = 1000 - (n % 1000)
if y == 1000:
    y = 0
print(y)