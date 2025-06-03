S = input()
n = len(S) + 1
a = [0] * n

S = ('<' if S[0] == '>' else '>') + S \
    + ('<' if S[-1] == '>' else '>') # 最初と最後にダミー追加、長さn+1
    
for i in range(n):
    if S[i : i + 2] == '><': # 極小値
        for j in range(i, 0, -1):   # 左に辿る
            if S[j] == '<': break
            a[j - 1] = max(a[j - 1], a[j] + 1)
        for j in range(i + 1, n):   # 右に辿る
            if S[j] == '>': break
            a[j] = max(a[j], a[j - 1] + 1)

print(sum(a))