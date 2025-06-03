N = int(input())
a = [int(x) for x in input().split()]

count = 0

for i in range(N):
    if i == 0 or i % 2 == 0:
        if a[i] % 2 != 0:
            count += 1

print(count)