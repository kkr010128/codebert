i,j=map(int,input().split())
listA=[]
for n in range(i):
    listA.append(list(map(int,input().split())))
    listA[n].append(sum(listA[n]))
listA.append([])
for n in range(j+1):
    number=0
    for m in range(i):
        number+=listA[m][n]
    listA[i].append(number)
for n in range(i+1):
    print(' '.join(map(str,listA[n])))
