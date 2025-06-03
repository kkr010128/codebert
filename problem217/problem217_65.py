n=int(input())
a=list(map(int,input().split()))

l=[]
flag=0
for aa in a:
  if aa%2==0:
    flag=1
    l.append(aa)

if flag==1:   
  for ll in l:
    if ll % 3!=0 and ll % 5!=0:
	    flag=2

if flag==0:
  print('APPROVED')
elif flag==1:
  print('APPROVED')
elif flag==2:
  print('DENIED')
