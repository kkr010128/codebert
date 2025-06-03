N = int(input())
A = list(map(int, input().split()))
B = [0 for i in range(N)]
for a in A:
  B[a-1] += 1
s = 0
for b in B:
  s += b * (b-1) // 2
for a in A:
  print(s - (B[a-1]-1))