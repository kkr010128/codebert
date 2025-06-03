N=int(input())
x=input()
num=0
n=0
def twice(a):
    ans=0
    while a:
        ans+=a%2
        a//=2
    return ans

ma=5*10**5
dp=[0]*ma
for i in range(1,ma):
    dp[i]=dp[i%twice(i)]+1
c=x.count("1")
a=int(x,2)%(c+1)
if c==1:
    for i in range(N):
        if x[i]=="0":
            print(dp[(a+pow(2,N-i-1,2))%2]+1)
        else:
            print(0)
    exit()
b=int(x,2)%(c-1)
for i in range(N):
    if x[i]=="0":
        print(dp[(a+pow(2,N-i-1,c+1))%(c+1)]+1)
    else:
        print(dp[(b-pow(2,N-i-1,c-1))%(c-1)]+1)