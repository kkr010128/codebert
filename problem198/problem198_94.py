n=int(input())

lis=[[[1,"a"]]]

for i in range(n-1):
    lisi=[]
    for j in lis[i]:
        for k in range(j[0]):
            lisi.append([j[0],j[1]+chr(ord("a")+k)])
        lisi.append([j[0]+1,j[1]+chr(ord("a")+j[0])])
    lis.append(lisi)

for i in lis[n-1]:
    print(i[1])