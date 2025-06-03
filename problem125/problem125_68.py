x = int(input())
y = x
while y % 360:
    y += x
print(y//x)