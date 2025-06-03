n=int(input())
cnt=0
a=1
while(a*a<n):
    cnt+=1
    cnt+=max((n-1)//a-a,0)*2
    a+=1
print(cnt)