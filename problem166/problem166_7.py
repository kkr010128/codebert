s=list(input())
l=[0]*2019
t=0
ans=0
for i in range(len(s)):
    t=(t+pow(10,i,2019)*int(s[-1-i]))%2019
    l[t]+=1
for i in l:
    ans+=(i*(i-1))//2
print(ans+l[0])