k = int(input())

a = [7 % k]
if a[0] == 0:
    print(1)
    exit()
for i in range(1, k):
    a.append((10*a[i - 1] + 7) % k)
    if a[i] % k == 0:
        print(i + 1)
        exit()

print(-1)