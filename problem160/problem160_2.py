n,m,q = map(int,input().split())
a = [0]*q
b = [0]*q
c = [0]*q
d = [0]*q
for i in range(q):
    a[i], b[i], c[i], d[i] = map(int, input().split())
    a[i] -= 1 # インデックス補正
    b[i] -= 1 
    
def score(A):
    x = 0
    for ai,bi,ci,di in zip(a,b,c,d):
        if A[bi] - A[ai] == ci:
            x += di
    return x

def dfs(A):
    # 終端条件 --- 3 重ループまで回したら処理して打ち切り
    if len(A) == n:
        #print(A)
        return score(A)
    res = 0
    # 単調増加するように制限
    pre = A[-1] if len(A) > 0 else 0 
    for v in range(pre, m):
        A.append(v) # 次のノードへの遷移
        res = max(res,dfs(A))      # 再帰呼出し
        A.pop()     # 一回元に戻す (これが結構ポイント appendする前の状態に戻している)
    return res

print(dfs([]))