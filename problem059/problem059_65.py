(r, c) = [int(i) for i in input().split()]

a = []
for i in range(r):
    a.append([int(i) for i in input().split()])
a.append([0 for i in range(c)])

for i in range(r + 1):
    sum = 0
    count = 0
    for j in a[i]:
        print(j, end=' ')
        sum += j
        if i != r:
            a[r][count] += j
            count += 1
    print(sum)