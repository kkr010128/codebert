import sys
sys.setrecursionlimit(10**8)

n = int(input())
x = list(input())
bit_cnt = x.count('1')

# bitを一つ増やす場合
pos = [0] * n
pos_total = 0

# bitを一つ減らす場合
neg = [0] * n
neg_total = 0

base = 1
for i in range(n):
    pos[-i-1] = base%(bit_cnt+1)
    if x[-i-1] == '1':
        # 同時にmod(bit_cnt+1)の法でトータルを作成
        pos_total = (pos_total + base) % (bit_cnt+1)
    base = (base*2) % (bit_cnt+1)

base = 1
if bit_cnt == 1:
    # mod取れない
    pass
else:
    for i in range(n):
        neg[-i-1] = base%(bit_cnt-1)
        if x[-i-1] == '1':
            # 同時にmod(bit_cnt-1)の法でトータルを作成
            neg_total = (neg_total + base) % (bit_cnt-1)
        base = (base*2) % (bit_cnt-1)

def popcount(n):
    s = list(bin(n)[2:])
    return s.count('1')

memo = {}
memo[0] = 0
def dfs(n, depth=0):
    if n in memo:
        return depth + memo[n]
    else:
        ret = dfs(n%popcount(n), depth+1)
        # memo[n] = ret
        return ret

ans = []
for i in range(n):
    if x[i] == '0':
        st = (pos_total + pos[i]) % (bit_cnt+1)
        print(dfs(st, depth=1))
    elif bit_cnt == 1:
        # コーナーケース：すべてのbitが0となる
        print(0)
    else:
        st = (neg_total - neg[i]) % (bit_cnt-1)
        print(dfs(st, depth=1))
