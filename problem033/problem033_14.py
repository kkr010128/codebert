d=input().split()
for o in input():
 s={'N':(1,5,2,3,0,4),'W':(2,1,5,0,4,3),'E':(3,1,0,5,4,2),'S':(4,0,2,3,5,1)}[o]
 d=[d[i]for i in s]
print(d[0])
