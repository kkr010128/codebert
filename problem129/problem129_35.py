N = int(input())
A = list(map(int, input().split()))
# ex. 24 11 8 3 16
A.sort()
# ex. 3 8 11 16 24
cnt = 0
# Aの最大値が24なら25個用意する感じ
# indexと考える値を一致させて分かりやすくしている
# Trueで初期化
# 最後のインデックスはA[-1]
dp = [True] * (A[-1] + 1)

# エラトステネスの篩っぽいやつ
for i in range(N):
    if dp[A[i]] == True:
        # dp[A[i]], dp[2*A[i]], dp[3*A[i]],...をFalseにする
        for j in range(A[i], A[-1] + 1, A[i]):
            dp[j] = False

        if i < N - 1:
            # 次も同じ数字が存在するなら数えない、なぜならお互いに割れてしまって題意を満たさないから
            # 次以降に出てくる同じ数字は既にFalseになっているのでもう走査する事はない
            if A[i] != A[i + 1]:
                cnt += 1
        # i=N-1の時は次がないので無条件でcntを増やす
        # elseの方が良さそうだが明示的にするためにelifを使った
        elif i == N - 1:
            cnt += 1

print(cnt)
