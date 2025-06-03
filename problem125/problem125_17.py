x = int(input())
y = 0
k = 0
while True:
    y += x
    k += 1
    if y % 360 == 0:
        break
print(k)