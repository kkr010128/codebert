x = int(input())

for i in range(x):
    if 105 * i >= x >= 100 * i:
        print(1)
        exit()

print(0)
