k=int(input())
a=[]
judge=0
a.append("")
a.append(7%k)
for i in range(2,k+1):
    a.append((a[i-1]*10+7)%k)
for i in range(1,k+1):
    if a[i]==0:
        print(i)
        judge=1
        break
if judge==0:
    print(-1)

