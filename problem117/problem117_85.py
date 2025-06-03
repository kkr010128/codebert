from bisect import bisect


N, M, K = map(int, input().split())
A = map(int, input().split())
B = map(int, input().split())

a_cum = [0]
cum = 0
for x in A:
  cum += x
  a_cum.append(cum)
  
b_cum = []
cum = 0
for x in B:
  cum += x
  b_cum.append(cum)
  
answer = 0

for i, a in enumerate(a_cum):
  remain = K - a
  if remain < 0:
    break

  t = bisect(b_cum, remain)
  # print('remain', remain, 't', t)
  answer = max(answer, i + t)
  
      
print(answer)    