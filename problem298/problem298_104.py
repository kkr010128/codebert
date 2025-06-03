N, k = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]
s = 0
for i in h:
    if i >= k:
        s += 1
print(s)