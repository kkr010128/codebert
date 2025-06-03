N = int(input())
an = list(map(int, input().split()))
count = 0

for i in range(N):
    if (i+1) % 2 != 0:
        if an[i] % 2 != 0:
            count += 1

print(count)