n = int(input())

lis =[]
for i in range(1,n+1):
    lis.append(i)
    
odd =[]
for j in lis:
    if j % 2 != 0:
        odd.append(j)
        
print(len(odd)/len(lis))