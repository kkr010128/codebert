n = int(input())
tp = ((1,1),(1,-1))
for i in range(200):
    for j in range(200):
        for k in tp:
            a,b = i*k[0],j*k[1]
            if((a**5 - b**5)==n):
                print(a,b)
                exit()