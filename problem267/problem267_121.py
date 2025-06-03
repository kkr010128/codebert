N=int(input())
S=input()
ans=0
for i in range(1000):
    one=str(i//100)
    two=str((i%100)//10)
    three=str(i%10)
    f1,f2,f3=False,False,False
    ptr=0
    for j in range(ptr,N-2):
        if S[j]==one:
            f1=True
            ptr=j+1
            break
    if f1:
        for j in range(ptr,N-1):
            if S[j]==two:
                f2=True
                ptr=j+1
                break
        if f2:
            for j in range(ptr,N):
                if S[j]==three:
                    f3=True
                    ans+=1
                    break
print(ans)