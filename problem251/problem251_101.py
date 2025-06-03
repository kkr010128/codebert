# 筐体の手が'k'回前と同じ場合, その回は勝てないが, 'k'回後は勝てる
# 筐体が出した各回の手をメモ, ただし'k'回前と同じ場合のみ ’-1’をメモする
# 勝ち手が'k'回前と同じ場合は加算なし, それ以外('-1'を含む)は勝ち点を加算 

n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()

ans = 0
memo = []
for i in range(n):
    if i < k or t[i] != memo[i-k]:
        memo.append(t[i])
        if t[i] == 'r': ans += p
        elif t[i] == 's': ans += r
        else: ans += s

    else:
        memo.append('-1')

print(ans)
