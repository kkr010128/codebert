a=[]
for i in range(3):
  da=list(map(int,input().split()))
  for j in da:
    a.append(j)
n=int(input())
for i in range (n):
  b=int(input())
  for j in range(len(a)):
    if a[j] == b:
      a[j]=0

for i in range (3):
  if a[i] == a[i+3] and a[i+3]==a[i+6]:
    print('Yes')
    exit()
for i in range(3):
  if a[3*i]==a[3*i+1] and a[3*i]==a[3*i+2]:
    print('Yes')
    exit() 
if a[0]==a[4] and a[0]==a[8]:
  print('Yes')
  exit()

if a[2]==a[4] and a[2]==a[6]:
  print('Yes')
  exit()
print('No')