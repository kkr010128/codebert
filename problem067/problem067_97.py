turn=int(input())
duel=[input().split(" ")for i in range(turn)]
point=[0,0]
for i in duel:
    if i[0]==i[1]:
        point[0],point[1]=point[0]+1,point[1]+1
    if i[0]>i[1]:
        point[0]+=3
    if i[0]<i[1]:
        point[1]+=3
print(" ".join(map(str,point)))
