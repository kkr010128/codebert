


N = int(input())
A = list(map(int, input().split()))


"""
indexのi,jについて、 j - i = A[i] + A[j] になる組の数を数え上げる。
愚直にやると、i,jを全ペアためす。N(O^2)で間に合わない

二つの変数が出てきて、ある式で関係性が表せる場合は、iの式 = jの式 みたいにしてやるとうまくいきことが多い
j - i = A[i] + A[j] 
-> A[i] + i = j - A[j]

なので、各参加者について、iとして使う時とjとして使うときで分けて数えていって、最後に組の数を数え上げる
A[i], i >=1 なので、２以上
1 <= j <= N, A[j] >= 1 なので、N未満
の範囲を調べればよい
"""
from collections import defaultdict
I = defaultdict(int)
J = defaultdict(int)

for i in range(N):
    I[A[i] + i+1] += 1
    J[i+1 - A[i]] += 1

ans = 0
for i in range(2, N):
    ans += I[i] * J[i]

print(ans)