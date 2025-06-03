s=input()
q=int(input())
cnt=0
front=[]
rear=[]
for qq in range(q):
  l=list(input().split())
  if l[0]=='1':
    cnt+=1
  else:
    if (cnt+int(l[1]))%2==1:
      front.append(l[2])
    else:
      rear.append(l[2])
front=''.join(front[::-1])
rear=''.join(rear)
s=front+s+rear
print(s if cnt%2==0 else s[::-1])