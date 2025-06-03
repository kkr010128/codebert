n=int(input())
data=list(map(int,input().split()))
data=sorted(data)
flag=0
for i in range(len(data)-1):
    if data[i]==data[i+1]:
        flag=1
        break
if flag==1:
    print("NO")
else:
    print("YES")