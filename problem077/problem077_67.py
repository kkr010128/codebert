# B 
z = list(map(int, input().split(" ")))
maxnum = z[0]*z[2]
for i in range(2):
    for j in range(2):
        x = z[i]
        y = z[j+2]
        prod = x*y
        # print(x, y, prod, maxnum, prod > maxnum)
        if prod > maxnum:
            maxnum = prod
print(maxnum)