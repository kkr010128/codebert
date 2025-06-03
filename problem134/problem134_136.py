n = int(input())

a = sorted(list(map(int, input().split())))

x = 1

for i in range(n):
    x = x * a[i]
    if x == 0:
        break
    elif x > 10 ** 18:
        x = -1
        break

print(x)
