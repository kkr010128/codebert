list =[]
i=0
index=1

while(index != 0):
    index=int(input())
    list.append(index)
    i +=1

for i in range(0,i):
    if list[i] == 0:
        break
    print("Case",i+1,end='')
    print(":",list[i])
