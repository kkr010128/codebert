X = int(input())
i = 1
while (360 * i) % X != 0: i += 1
print((360 * i) // X)