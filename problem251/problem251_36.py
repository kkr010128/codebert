def solve():
  N, K = map(int, input().split())
  R, S, P = map(int, input().split())
  dic = {'r':P,'s':R,'p':S}
  T = input()
  point = [0]*N
  for i in range(N):
    if i<K:
      point[i] = dic[T[i]]
    else:
      if T[i]!=T[i-K] or point[i-K]==0:
        point[i]=dic[T[i]]
  ans = sum(point)
  return ans
print(solve())