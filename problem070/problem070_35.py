# coding: utf-8
N, Q = map(int,input().split())
#N,Q=map(int,input().split())
#親のノードを格納　2の親が4のとき par[2]=4
par=[0]
#木の深さを格納　根が2の深さが3の時 rank[2]=3
rank=[0]

#初期化
for i in range(1,N+1):
    par.append(i)
    rank.append(0)

#xの根を探す、同時に通過したノードすべてを根に直接つける
def find(x):
    #xの親がxならば根なのでxを返す
    if par[x]==x:
        return x
    else:
        #違う場合は親の親を捜し自分の親にする
        par[x] = find(par[x])
        #再帰的に行うと根が見つかる
        return par[x]

#xが属する木とyが属する木を併合する
def unite(x,y):
    #根を探す
    root_x=find(x)
    root_y=find(y)

    #根が同じなら元からつながっているので終わり
    if root_x == root_y:
        return

    #ランクが大きい木の根の直下にランクが小さい木を結合
    if rank[root_x] < rank[root_y]:
        par[root_x] = root_y

    else:
        par[root_y] = root_x

    #ランクが等しいときのみランクが増える#なぜ#yにxが結合？
    if rank[root_x]==rank[root_y]:
        rank[root_x]+=1

#xとyが同じ木に存在するかを調べる
def same(x,y):
    return find(x)==find(y)

#main
for i in range(Q):
    a,b=map(int,input().split())
    unite(a, b)
res = []
for i in range(1, N+1):
    res.append(find(i))
ans = len(set(res))-1
print(ans)