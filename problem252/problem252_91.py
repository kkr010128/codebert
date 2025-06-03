N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()

def condition(num):
    count=0
    s=N-1
    t=0
    while N-1>=t and s>=0:
        if num>A[s]+A[t]:
            t+=1
        else:
            count+=N-t
            s-=1
    return count>=M

subans=0
start=1
end=2*A[N-1]
while end-start>1:
    test=(end+start)//2
    if condition(test):
        start=test
    else:
        end=test
if condition(end):
    subans=end
else:
    subans=start

data=[0]*N
count=0
s=N-1
t=0
while N-1>=t and s>=0:
    if subans>A[s]+A[t]:
        t+=1
    else:
        count+=N-t
        data[s]=2*(N-t)
        s-=1

ans=sum(data[i]*A[i] for i in range(0,N))
if count>M:
    ans-=(count-M)*subans
print(ans)
