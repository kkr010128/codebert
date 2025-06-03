s=input()
q=int(input())

cnt=0
left=""
right=""

for i in range(q):
  qq=[x for x in input().rstrip().split()]

  if qq[0]=="2":
    t=int(qq[0])
    f=int(qq[1])
    c=qq[2]
    
    if cnt%2==1 and f==1:
      right=right+c
    
    elif cnt%2==1 and f==2:

      left=c+left
    elif cnt%2==0 and f==2:
  
      right=right+c
    elif cnt%2==0 and f==1:

      left=c+left

  else:
    cnt+=1

s=left+s+right
if cnt%2==1:
  print(s[::-1])
else:
  print(s)