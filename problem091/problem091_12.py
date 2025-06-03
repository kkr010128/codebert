n = int(input())
l = sorted([int(i) for i in input().split(' ')])

if len(l) < 3:
    print(0)
    exit()

count = 0

for i in range(0, (n - 2)):
    for j in range((i + 1), (n - 1)):
        if l[i] == l[j]:
            continue
        for k in range((j + 1), n):
            if l[j] == l[k]:
                continue

            if l[i] + l[j] > l[k]:
                count += 1

print(count)