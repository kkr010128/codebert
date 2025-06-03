a=[]
for i in range(2):
    m=input().split()
    a.append(m)

list_1=[int(l) for l in a[0]]
list_2=[int(l) for l in a[1]]
total=0
largest=list_2[0]
smallest=list_2[0]


for x in range(list_1[0]):
    if largest<list_2[x]:
        largest=list_2[x]
    if smallest>list_2[x]:
        smallest=list_2[x]

for x in list_2:
    total+=x

print(smallest,largest,total)