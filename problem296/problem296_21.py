S = input()
K = int(input())

# S単体で必要な置換数を求める
cnt = 0
for i in range(len(S)-1):
    if S[i] == S[i+1]:
        cnt += 0.5
    else:
        cnt = int(cnt+0.5)
cnt = int(cnt+0.5)

# Sを接続した時に必要な置換数を求める
s3 = S*3
cnt_1 = 0
for i in range(len(s3)-1):
    if s3[i] == s3[i+1]:
        cnt_1 += 0.5
    else:
        cnt_1 = int(cnt_1+0.5)
cnt_1 = int(cnt_1+0.5)

# 単体と接続時に必要な置換数の合計を求める
ans = int((cnt_1-cnt*3)/2*(K-1)+0.5)+cnt*K
print(ans)
