count = 0
for i in range(1, int(input()) + 1):
    if not(i % 5 == 0) and not(i % 3 == 0):
        count = count + i

print(count)


