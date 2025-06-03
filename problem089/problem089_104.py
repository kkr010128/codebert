h,w,m=map(int,input().split())
HW=[list(map(int,input().split())) for _ in range(m)]

H,W=[0 for _ in range(h)],[0 for _ in range(w)]
for i,j in HW:
    i,j=i-1,j-1
    H[i] +=1
    W[j] +=1

max_h,max_w=max(H),max(W)
ans=max_h+max_w
cnt=H.count(max_h)*W.count(max_w)
for i,j in HW:
    if H[i-1]==max_h and W[j-1]==max_w:
        cnt -=1
print(ans if cnt!=0 else ans-1)