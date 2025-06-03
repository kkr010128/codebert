N = int(input())
A = list(map(int,input().split()))
Q = int(input())
S = [list(map(int, input().split())) for l in range(Q)]
 
numList = {}
sum = 0

for n in range(N):
  if A[n] not in numList:
    numList[A[n]] = 0
  numList[A[n]] += 1
  sum += A[n]

for q in range(Q):
  if S[q][0] in numList:
    if S[q][1] not in numList:
      numList[S[q][1]] = 0
    sum += (S[q][1] - S[q][0]) * numList[S[q][0]]
    numList[S[q][1]] += numList[S[q][0]]
    numList[S[q][0]] = 0
  print(sum)