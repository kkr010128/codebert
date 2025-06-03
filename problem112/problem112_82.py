from collections import deque #両端から取り出すのが速い
N,K = map(int,input().split())
A = list(map(int,input().split()))
pos = []
neg = []
for a in A:
    if a >= 0:
        pos.append(a)
    else:
        neg.append(-a)
pos = deque(sorted(pos))
neg = deque(sorted(neg))
mod = 10**9+7
ans = 1
sign = 1
if K%2 == 1: #Kが奇数の時pos（ある場合）から必ず１つ取る
    if len(pos) > 0:
        ans = ans*pos.pop() % mod
    else:
        ans = ans*neg.popleft() % mod
        sign *= -1
    K -= 1
while K > 0: #偶数の場合と奇数の残りの処理
    if len(pos) == 1 and len(neg) == 1:
        ans = ans*-neg.pop()*pos.pop() % mod
    elif sign == 1:#通常バージョン
        if len(pos) < 2 or (len(neg) >= 2 and pos[-2]*pos[-1] < neg[-2]*neg[-1]):
            ans = ans*neg.pop()*neg.pop() % mod
        else:
            ans = ans*pos.pop()*pos.pop() % mod
    else:#奇数の前処理で負になっている場合(最終結果も負になるので小さくしたい)
        if len(pos) < 2 or (len(neg) >= 2 and pos[-2]*pos[-1] < neg[-2]*neg[-1]):
            ans = ans*neg.popleft()*neg.popleft() % mod
        else:
            ans = ans*pos.popleft()*pos.popleft() % mod
    K -= 2
ans = ans*sign % mod
print(ans)

