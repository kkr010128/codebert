h,w= map(int,input().split())
tb = [input() for _ in range(h)]
st = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if i==0 and j==0:st[i][j]= (1 if tb[i][j]=='#' else 0)
        else:
            tr=td=999999999
            if i!=0:
                td=st[i-1][j]+(1 if (tb[i-1][j]=='.' and tb[i][j]=='#') else 0)
            if j!=0:
                tr=st[i][j-1]+(1 if (tb[i][j-1]=='.' and tb[i][j]=='#') else 0)
            st[i][j]=min(td,tr)
print(st[h-1][w-1])