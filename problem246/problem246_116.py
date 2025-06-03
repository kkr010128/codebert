import bisect
N = int(input())
Kaijo = [1 for _ in range(N)]
for i in range(2,N+1):
  Kaijo[-i] = Kaijo[1-i]*i
#print(Kaijo)
L = [i+1 for i in range(N)]
P = list(map(int,input().split()))
PN = 0
for i in range(N-1):
  k = bisect.bisect_left(L, P[i])
  L.remove(P[i])
  PN += k*Kaijo[i+1]
#print(PN)
L = [i+1 for i in range(N)]
Q = list(map(int,input().split()))
QN = 0
for i in range(N-1):
  k = bisect.bisect_left(L, Q[i])
  L.remove(Q[i])
  QN += k*Kaijo[i+1]
ans = abs(PN-QN)
print(ans)