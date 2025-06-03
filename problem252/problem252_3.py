import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

# ある値以上のAiがいくつあるかの情報を累積和で保持
num_A_or_more = [0]*(10**5)
for a in A:
  num_A_or_more[a-1] += 1


for i in range(1, 10**5):
  j = 10**5 - i
  num_A_or_more[j-1] += num_A_or_more[j]


# x以上となる手の組み合わせがM種類以上あるかどうかを判定
def check(x):
  count = 0
  for a in A:
    idx = max(x-a-1, 0)
    if idx >= 10**5:
      continue
    count += num_A_or_more[idx]
  
  return count>=M


# 2分探索でM種類以上の手の組み合わせがある満足度の最大値を求める
left = 0
right = 2*10**5 + 1
mid = (left + right) // 2
while right - left > 1:
  if check(mid):
    left = mid
  else:
    right = mid
    
  mid = (left + right)//2

# これがM種類以上の手の組み合わせがある満足度の最大値
x = left


# 降順に並べなおして累積和を求めておく
rev_A = A[::-1]
accum_A = [rev_A[0]]
for i, a in enumerate(rev_A):
  if i == 0:
    continue
  accum_A.append(accum_A[-1] + a)

ans = 0
count = 0
surplus = 2*10**5 # M種類を超えた場合は、一番小さくなる握手の組を最後に削る
for ai in rev_A:
  idx = bisect.bisect_left(A, x-ai)
  if idx == N:
    break
  ans += (N-idx)*ai + accum_A[N-idx-1]
  count += N - idx
  surplus = min(surplus, ai+A[idx])


print(ans - (count-M)*surplus)