n, d = map(int, input().split())


number = 0
for i in range(n):
    x, y = map(int, input().split())
    distance = x ** 2 + y ** 2
    
    if distance <= d ** 2:
        number += 1

print(number)