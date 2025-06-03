l=[0]+[int(i) for i in input()]
l.reverse()
su=0
for i in range(len(l)):
    if l[i]>5:
        l[i]=10-l[i]
        l[i+1]+=1
    elif l[i]==5 and l[i+1]>4:
        l[i+1]+=1
    su+=l[i]
print(su)