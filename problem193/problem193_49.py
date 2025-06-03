h,w,k=map(int,input().split())
S=[input() for i in range(h)]

LIS=[]

def saiki(x,st):
    if x==h-1:
        LIS.append(st)
        return
    else:
        saiki(x+1,st+st[-1])
        saiki(x+1,st+str(int(st[-1])+1))

saiki(0,"0")

DIC1={c:0 for c in "0123456789"}
DIC2={c:0 for c in "0123456789"}
ans=10**9
for cod in LIS:
    for ele in DIC1:
        DIC1[ele]=0
    cnt=int(cod[-1])
    end=False
    for i in range(w):
        for ele in DIC2:
            DIC2[ele]=0
        for q in range(h):
            if S[q][i]=="1":
                DIC2[cod[q]]+=1
        if max(DIC2.values())>k:
            end=True
            break
        flg=True
        for ele in DIC1:
            if DIC1[ele]+DIC2[ele]>k:
                flg=False
                break
        if flg:
            for ele in DIC1:
                DIC1[ele]+=DIC2[ele]
        else:
            for ele in DIC1:
                DIC1[ele]=DIC2[ele]
            cnt+=1
    if end:
        continue
    ans=min(ans,cnt)
    #print(cod,cnt)
print(ans)
