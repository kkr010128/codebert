import sys,math
input = sys.stdin.readline

n,k = map(int,input().split())
a = [int(i) for i in input().split()]
f = [int(i) for i in input().split()]
a.sort()
f.sort(reverse=True)
c = [(i*j,j) for i,j in zip(a,f)]
m = max(c)

def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    chk = 0
    for i,j in c:
      chk += math.ceil(max(0,(i-arg))/j)
    return chk <= k


def bisect_ok(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義
    ng = 最小の値-1 ok = 最大の値+1 で最小
    最大最小が逆の場合はng ok をひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
  
print(bisect_ok(-1,m[0]+1))