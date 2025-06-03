bingo=[]
for i in range(3):
  a=list(map(int,input().split()))
  bingo.append(a)
  
n=int(input())
for i in range(n):
  b=int(input())
  for j in range(3):
    if b in bingo[j]:
      bingo[j][bingo[j].index(b)]=0
      
def hantei(l):
  for i in range(3):
    if all([l[i][j]==0 for j in range(3)]):
      return 'Yes'
    
    elif all([l[j][i]==0 for j in range(3)]):
      return 'Yes'
    
    elif l[0][0]==0 and l[1][1]==0 and l[2][2]==0:
      return 'Yes'
    
    elif l[0][2]==0 and l[1][1]==0 and l[2][0]==0:
      return 'Yes'
    
    else:
      continue
      
  return 'No'
    
#print(bingo)
print(hantei(bingo))