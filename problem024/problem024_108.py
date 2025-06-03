n,k=map(int,input().split())

W=[int(input()) for _ in range(n)]

def Wcheck(W,P,k):
    i=0
    for j in range(k):
        temp_w=0
        while temp_w+W[i]<=P:
            temp_w=temp_w+W[i]
            i=i+1
            if i==len(W):
                return len(W)

    return i

def PSearch(W,start,end,k):
    if start==end:
        return start
    mid=(start+end)//2
    v=Wcheck(W,mid,k)
    if v>=n:
        return PSearch(W,start,mid,k)
    else:
        return PSearch(W,mid+1,end,k)

print(PSearch(W,0,1000000000,k))
