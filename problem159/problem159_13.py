x = int(input())
y = 0
z = 100

while z<x:
    y+=1
    z *= 101
    z //= 100

print(y)