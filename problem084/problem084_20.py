def main():
    import sys
    input = sys.stdin.readline


    #Union Find

    #xの根を求める
    def find(x):
        if par[x] < 0:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    #xとyの属する集合の併合
    def unite(x,y):
        x = find(x)
        y = find(y)
        
        if x == y:
            return False
        else:
            #sizeの大きいほうがx
            if par[x] > par[y]:
                x,y = y,x
            par[x] += par[y]
            par[y] = x
            return True

    #xとyが同じ集合に属するかの判定
    def same(x,y):
        return find(x) == find(y)

    #xが属する集合の個数
    def size(x):
        return -par[find(x)]

    n,m = map(int,input().split())
    #初期化
    #根なら-size,子なら親の頂点
    par = [-1]*n

    for i in range(m):
        X,Y = map(int,input().split())
        unite(X-1,Y-1)
    
    #tank = set([])
    for i in range(n):
        find(i)
    ans=0
    for i in par:
        if i<0:
            ans=max(ans,-i)
    print(ans)

if __name__ == '__main__':
    main()
