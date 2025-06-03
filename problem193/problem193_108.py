h,w,k= map(int, input().split())
s = [[int(i) for i in input()] for i in range(h)]

for i in range(h):
    for j in range(1,w):
        s[i][j]+=s[i][j-1]

for i in range(w):
    for j in range(1,h):
        s[j][i]+=s[j-1][i]

#　１行目、一列目をゼロにする。
s=[[0]*w]+s
for i in range(h+1):
    s[i]=[0]+s[i]

ans=float('inf')
#bit 全探索
for i in range(2**(h-1)):
    line=[]
    for j in range(h-1):
        if (i>>j)&1:
            line.append(j+1)
    cnt=len(line)
    line=[0]+line+[h]
    x=0
    flag=True
    for k1 in range(1,w+1):
        v=0
        for l in range(len(line)-1):
            # どう分割してもダメな奴に✖︎のフラグ立てる
            if s[line[l+1]][k1]-s[line[l+1]][k1-1]-s[line[l]][k1]>k:
                flag=False
                
            v=max(s[line[l+1]][k1]-s[line[l+1]][x]-s[line[l]][k1]+s[line[l]][x],v)
            
        if v>k:
            cnt+=1
            x=k1-1
            
    if flag:
        ans=min(cnt,ans)
        
print(ans)