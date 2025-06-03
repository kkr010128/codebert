main=list(map(int,input().split()));count=0
for i in range(main[0],main[1]+1):
    if(i%main[2]==0): count=count+1
print(count)