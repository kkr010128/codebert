a = input().split()
i = 0
for j in range(int(a[0]),int(a[1])+1):
    if (int(a[2]) % j) == 0:
        i = int(i) + 1

print(i)
