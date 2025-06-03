from collections import Counter
N = int(input())
A = list(map(int, input().split()))
L = [-1 for _ in range(N)]
R = [-1 for _ in range(N)]

for i in range(N):
  L[i] = A[i] - i-1
  R[i] = A[i] + i+1

# L = -R となる物のうち、i>jになりゃいいんだけど、最後にいくつかで破れば良い気がす
# i > 0 なので、自分自身を２回選んでL＝Rみたいにはならない・・・？

LC = Counter(L)
RC = Counter(R)

ans = 0
for k,v in LC.items():
  if (-1) * k in RC:
    ans += v * RC[(-1)*k]
    #print(k,v,(-1)*k,RC[(-1)*k], ans)
print(ans)

