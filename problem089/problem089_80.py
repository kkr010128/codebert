H,W,M=map(int,input().split())
h,w,bomb=[0]*H,[0]*W,[]
for i in range(M):
    a,b=map(int,input().split())
    bomb.append((a-1,b-1))
    h[a-1]+=1
    w[b-1]+=1
    
max_h=max(h)
max_w=max(w)

bomb_and_max=0
for i,j in bomb:
    if h[i]==max_h and w[j]==max_w:
        bomb_and_max+=1
    
if bomb_and_max==h.count(max_h)*w.count(max_w):
    print(max_h+max_w-1)
else:
    print(max_h+max_w)