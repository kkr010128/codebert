n = int(input())
l = list(map(int,input().split()))

h = 0
sum = 0
for i in range(n):
    if l[i] <= h:
        sum += h - l[i]
    else:
        h = l[i]

print(sum)
