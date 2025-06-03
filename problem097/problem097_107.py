k = int(input())
value = 7

for i in range(1, 10 ** 6):
    if value % k == 0:
        print(i)
        exit()
    value = (value * 10 + 7) % k
print(-1)