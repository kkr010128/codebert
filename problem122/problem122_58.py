n = int(input())
A = list(map(int, input().split()))
S = sum(A)
D = {c:0 for c in range(1, 10**5+1)}
for a in A:
  D[a] += 1
for _ in range(int(input())):
  B, C = map(int, input().split())
  S += (C-B)*D[B]
  D[C] += D[B]
  D[B] = 0
  print(S)