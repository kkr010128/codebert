import sys
from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, *A = map(int, read().split())

memo = defaultdict(int)  # 0で初期化する
answer = 0
for idx, x in enumerate(A, 1):  # indexを1から始める
    # i<jを満たしながらansを計算
    # idx = 1の時はansが増えることはない
    # idx = 2の時は、idx = 1の時の結果がmemoに記録されている
    # idx = 3の時は、idx=1,2の結果が記録されている
    # 以下同様
    answer += memo[idx - x]
    memo[idx + x] += 1

print(answer)
