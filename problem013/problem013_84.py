n = int(input())
l = [int(input()) for _ in range(n)]

minval = l[0]
maxp = -1000000000
for val in l[1:]:
    if maxp < val - minval:
        maxp = val - minval
    if minval > val:
        minval = val

print(maxp)

