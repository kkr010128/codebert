N=list(input())
M=list(input())
ans=0
number=len(N)
for i in range(number):
    if N[i]==M[i]:
        ans+=1
print(number-ans)