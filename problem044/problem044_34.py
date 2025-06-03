z = input()
a = list(map(int, z.split()))
cnt = 0
for i in range(a[0], a[1] + 1, 1):
    if a[2] % i == 0:
        cnt += 1
print(cnt)