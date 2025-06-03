r, g, b = map(int, input().split())
t = 0
while r >= g: g *= 2; t += 1
while g >= b: b *= 2; t += 1
print('No' if t > int(input()) else 'Yes')
