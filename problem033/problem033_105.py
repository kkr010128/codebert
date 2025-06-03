d=input().split()
for o in list(input()):
 s={'N':(0,1,5,4),'W':(0,2,5,3),'E':(0,3,5,2),'S':(0,4,5,1)}[o]
 for i in range(3):d[s[i+1]],d[s[i]]=d[s[i]],d[s[i+1]]
print(d[0])
