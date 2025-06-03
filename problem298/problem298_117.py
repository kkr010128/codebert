n,k = (int(x) for x in input().split())
h = [int(x) for x in input().split()]

count = 0

for i in range(len(h)):
    if k <= h[i]:
        count += 1

print(count)