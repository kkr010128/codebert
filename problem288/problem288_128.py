import math
N=int(input())
lim=int(math.sqrt(N))
ans=10**13
for i in range(1,lim+1):
    if N%i==0:
        if ans>(i+(N//i)-2):
            ans=(i+(N//i)-2)
print(ans)