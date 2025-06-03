x = int(input())

for i in range(-118, 120):
    for j in range(-119, i):
        if i ** 5 - j ** 5 == x:
            a = i
            b = j
print(a, b)