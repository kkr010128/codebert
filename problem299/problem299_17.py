N = int(input())
A = list(map(int, input().split()))
B = [0 for i in range(N)]
for i in range(N):
  B[A[i]-1] = i
for b in B:
  print(b+1)