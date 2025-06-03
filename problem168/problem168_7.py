N, M = map(int, input().split())
A = list(map(int, input().split()))
assert len(A) == M
# M個の宿題, それぞれAi日かかる
yasumi = N - sum(A)
if yasumi >= 0:
  print(yasumi)
else:
  print(-1)