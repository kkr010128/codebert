from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

MOD = 10**9 + 7

# 0以上の数
X = []
# 負の数
Y = []

# 左の方が絶対値が大きくなるようにそれぞれソート
for a in A:
    if a >= 0:
        X.append(a)
    else:
        Y.append(a)
X.sort(reverse=True)
X = deque(X)
Y.sort()
Y = deque(Y)
# print(X)
# print(Y)

nums = []
# 全部選ぶしかない場合
if K == N:
    nums = A
# どうやっても負にしかならない場合（Aが全て負 and Kが奇数）
# 絶対値が小さくなるように取っていく
elif len(Y) == N and K % 2 == 1:
    for _ in range(K):
        nums.append(Y.pop())
# 上記以外の場合、結果を0以上（負ではない）にすることが出来る
# 絶対値が大きくなるように and 負にならないように 取っていく
# X,Yについて、「2個以上ある場合」、「1個の場合」、「0個の場合」の3*3=9通りに分けられる
# Yが1個、0個の場合はまとめることが出来たので、結局3*2=6通り

# 残り1個しか追加出来ない時に注意

else:
    while len(nums) < K:
        if len(X) >= 2 and len(Y) >= 2:
            if X[0] * X[1] >= Y[0] * Y[1] or len(nums) == K - 1:
                nums.append(X.popleft())
            else:
                nums.append(Y.popleft())
                nums.append(Y.popleft())
        elif len(X) >= 2 and len(Y) <= 1:
            nums.append(X.popleft())

        elif len(X) == 1 and len(Y) >= 2:
            if X[0] >= Y[0] * Y[1] or len(nums) == K - 1:
                nums.append(X.popleft())
            else:
                nums.append(Y.popleft())
                nums.append(Y.popleft())
        elif len(X) == 1 and len(Y) <= 1:
            nums.append(X.popleft())

        elif len(X) == 0 and len(Y) >= 2:
            if len(nums) == K - 1:
                # 負にならざるを得ない場合、絶対値が小さい方の負の数を追加する(ここだけpopleftではなくpop)
                # 絶対に0以上に出来るという前提に矛盾しているが、形式上記述しておく
                nums.append(Y.pop())
            else:
                nums.append(Y.popleft())
                nums.append(Y.popleft())
        # K<=Nなので、共に0になることは起こり得ない
        elif len(X) == 0 and len(Y) <= 1:
            num.append(Y.pop())

ans = 1
for num in nums:
    ans *= num
    ans %= MOD
print(ans)
