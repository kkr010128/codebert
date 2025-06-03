n = int(input())

Robo = []
for i in range(n):
    x, l = map(int, input().split())
    Robo.append([x-l, x+l])
Robo.sort(key=lambda x: x[1])

#print(Robo)
biggest_right = 2 * -10**9 - 1
counter = 0
for left, right in Robo:
    if biggest_right <= left:
        counter += 1
        biggest_right = max(right, biggest_right)
print(counter)