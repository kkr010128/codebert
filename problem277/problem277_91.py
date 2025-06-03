H,W,K = map(int,input().split())
s=[list(input()) for i in range(H)]
area=[[0 for _ in range(W)] for _ in range(H)]

st_num=[0]*H
st_pos=[[] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if s[i][j]=="#":
            st_num[i] += 1
            st_pos[i].append(j)

upper=0
cnt=0
for i in range(H):
    if st_num[i]==0:
        upper=min(upper,i)
    else:
        cnt+=1
        
        #左の余白
        if st_pos[i][0]>0:
            for p in range(upper,i+1):
                for q in range(st_pos[i][0]):
                    area[p][q]=cnt
        #左端のいちごから右端のいちご左まで
        for j in range(st_num[i]-1):
            for p in range(upper,i+1):
                for q in range(st_pos[i][j],st_pos[i][j+1]):
                    area[p][q]=cnt
            cnt+=1
        #右端のいちごから右
        for p in range(upper,i+1):
            for q in range(st_pos[i][-1],W):
                area[p][q]=cnt                    
        upper = i+1
        
if upper!=H:  #下端のいちごよりも下の領域
    for p in range(upper,H):
        for q in range(W):
            area[p][q]=area[upper-1][q]                    
                
for i in area:
    print(*i)