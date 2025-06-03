S = input()
rain_d = 0
max_rain_d = 0
for s in S:
    if s == 'R':
        rain_d += 1
        max_rain_d = rain_d
    elif s == 'S':
        rain_d = 0
print(max_rain_d)