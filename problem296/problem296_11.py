s = input()
k = int(input())
def seqcnt(s):
    cnt=1
    ans=0
    bk=''
    for c in s+' ':
        if bk==c:
            cnt+=1
        else:
            ans+=(cnt)//2
            cnt=1
        bk=c
    return ans

cnt=seqcnt(s)
cnt2=seqcnt(s*2)    
if len(set(list(s)))==1:
    print(len(s)*k//2)
else:
    print(cnt+(cnt2-cnt)*(k-1))