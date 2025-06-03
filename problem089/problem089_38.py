H, W, M = map(int, input().split())
row=[0]*H #x座標を入れるっちゅうかカウント
col=[0]*W #y座標を入れる
 
mat=[] #座標を入れる
 
for i in range(M):
    h, w = map(int, input().split())
    row[h-1]+=1
    col[w-1]+=1
    mat.append((h-1,w-1))
r=max(row)
c=max(col)
 
rr=[1 if row[i]==r else 0 for i in range(H)] #maxな列のインデックス
cc=[1 if col[i]==c else 0 for i in range(W)] #maxな行のインデックス
 
x=0 #maxな列と行の交差点にある爆弾の個数をカウント
for k in mat:
    if rr[k[0]]==1 and cc[k[1]]==1:
        x+=1
        
if sum(rr)*sum(cc)==x: #行と列の全ての交差点に爆弾があれば-1する
    print(r+c-1)
else:
    print(r+c)