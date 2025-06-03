n,k,c=map(int,input().split())
s=input()
x,y=[0]*n,[0]*n
work1,work2=[],[]
last=-10**9;cnt=0
for i in range(n):
    if s[i]=="o" and i-last>c:
        cnt+=1
        last=i
        work1.append(i)
    if cnt==k: break

nextw=10**9;cnt=0
for i in range(n-1,-1,-1):
    if s[i]=="o" and nextw-i>c:
        work2.append(i)
        cnt+=1
        nextw=i
    if cnt==k: break

work2.reverse()
for i in range(k):
    if work1[i]==work2[i]: print(work1[i]+1)