D = int(input())

C = list(map(int, input().split()))

S = [list(map(int, input().split())) for i in range(D)]

L = [0 for i in range(26)]

T = [int(input()) for i in range(D)]

score=0

for d in range(D):
  score += S[d][T[d]-1]
  
  L[T[d]-1] = d+1
  down = 0
  for i in range(26):
    down+=C[i] * ((d+1) - L[i])

  score -=down
  
  print(score)