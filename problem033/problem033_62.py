houkou={'N':(1,5,2,3,0,4),'S':(4,0,2,3,5,1),'E':(3,1,0,5,4,2),'W':(2,1,5,0,4,3)}
saikoro=input().split()
for i in input():
  saikoro=[saikoro[j]for j in houkou[i]]
  #print(saikoro)
print(saikoro[0])
