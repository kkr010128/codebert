
N=int(input())
S=list(input())
numlist=range(1000)
ans=0

for i in numlist:
    num=str(i)
    if len(num)==1:
        num="00"+num
    if len(num)==2:
        num="0"+num
    if num[0] in S[:N-1]:
        num1=S.index(num[0])
        if num[1] in S[num1+1:N-1]:
            S2=S[num1+1:N-1]
            num2=S2.index(num[1])+num1+1
            if num[2] in S[num2+1:]:
                ans+=1
print(ans)