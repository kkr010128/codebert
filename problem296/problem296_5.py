# A - Connection and Disconnection
S = input()
K = int(input())
S = S + '1'# 番兵

# 連続する文字数をカウント
cnt = []
conti = 1
for i in range(1,len(S)):
    if S[i-1] == S[i]:
        conti += 1
    else:
        cnt.append(conti)
        conti = 1
        
# 最初と最後の文字が同じときの補正値
comp = 0
if S[0] == S[-2]:
    # 奇数個 + 奇数個のとき
    if cnt[0]%2 == 1 and cnt[-1]%2 == 1:
        comp = K - 1
    # S =aaa などのとき
    if len(set(S[:-1])) == 1 and len(S[:-1])%2 == 1:
        comp = K // 2
        
ans = [a//2 for a in cnt if a >= 2]
ans = sum(ans)*K + comp
print(ans)        