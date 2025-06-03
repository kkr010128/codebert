n=int(input())
p=list(map(int,input().split()))
min_num=p[0]
cnt=1
for i in range(1,len(p)):
    if p[i]<min_num:
        cnt+=1
        min_num=p[i]
print(cnt)