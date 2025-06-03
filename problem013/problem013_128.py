s = int(input())
maxv = -100000000000000000
minv = 10000000000000000

for i in range(s):
    x = int(input())
    maxv = max(maxv,x-minv)
    minv = min(minv,x)



if x >= 0:
    print(maxv)
else:
    print("-1")

