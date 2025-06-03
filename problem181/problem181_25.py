a=[str(i) for i in range(1,10)]
i=0
while len(a)<100000:
    if a[i][-1]!="0":
        a.append(a[i]+str(int(a[i][-1])-1))
    a.append(a[i]+str(int(a[i][-1])))
    if a[i][-1]!="9":
        a.append(a[i]+str(int(a[i][-1])+1))
    i+=1
# print(a[:30])
k=int(input())
print(a[k-1])