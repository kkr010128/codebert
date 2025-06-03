from collections import deque
 
n = int(input())

queue = deque([[1],[2],[3],[4],[5],[6],[7],[8],[9]]) # 初期化_ここでは正の一桁整数として'1'～'9'を設置
ptns = [] # パターン候補の器_初期化

while queue: # queueが空になるまでループ
    tmp = queue.popleft() # パターンの候補を popleft
    if len(ptns) < n: # ptnsの要素数が'n'個未満ならば append
        ptns.append(tmp)
    else:
        break
 # 以下、tmpに各々tmp[-1]-1、tmp[-1]、tmp[-1]+1をappendするための条件
    if tmp[-1] != 0:
        queue.append(tmp + [tmp[-1] -1])

    queue.append(tmp + [tmp[-1]])

    if tmp[-1] != 9:
        queue.append(tmp + [tmp[-1] +1])

# リスト = map(str, リスト) ← intのリストからstrのmapオブジェクトへ変換
print(''.join(map(str, ptns[-1])))