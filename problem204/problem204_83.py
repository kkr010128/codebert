S=input()
Q=int(input())
Q=[input().split() for i in range(Q)]
Forward=[]
Backward=[]
count=0
for i in Q:
    if i[0]=='1':
        count+=1
    else:
        if (int(i[1])+count)%2==1:
            Forward.append(i[2])
        else:
            Backward.append(i[2])  
if count%2==0:
    ans = (''.join(Forward))[::-1]+S+(''.join(Backward))
else:
    ans = (''.join(Backward)[::-1]+S[::-1]+(''.join(Forward)))
print(ans)