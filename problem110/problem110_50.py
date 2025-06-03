import copy

H,W,K = input().split()
H = int(H)
W = int(W)
K = int(K)
c = list(input() for i in range(H))
for j in range(H):
    c[j] = list(c[j])
    
def wise(a,masu):#a行の塗りつぶし
    for w in range(W):
        masu[a][w] = 'r'
    return masu
        
def hight(b,ban):#b列の塗りつぶし
    for h in range(H):
        ban[h][b] = 'r'    
    return ban

count = 0
#2**(H+W)は2進数で1 << (H+W)と書ける
for j in range(1<<(H+W)):
    bunsin = copy.deepcopy(c)#コピーを定義しておくことでCの形を戻す
    for k in range((H+W)):
        mask = 1 << k
        if j & mask != 0:
            if k < W:#列の処理
                hight(k, bunsin)
                
            else :#行の処理
                wise(k - W, bunsin)
              
    new_c = []
    for l in range(H):#copyから'#を取り出す'
        for m in range(W):
            new_c.append(bunsin[l][m])
    count_black = new_c.count('#')
    if count_black == K:
        count += 1
print(count)