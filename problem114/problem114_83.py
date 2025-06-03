D = int(input())
C = list(map(int, input().split()))
S = list(list(map(int, input().split())) for i in range(D))
T = list(int(input()) for i in range(D))
manzoku = 0
yasumi= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#1日目
for day in range(D):
  yasumi = list(map(lambda x: x + 1, yasumi))
  yasumi[T[day] - 1] = 0
  manzoku += S[day][T[day] - 1]
  for i in range(26):
    manzoku -= C[i] * yasumi[i]
  print(manzoku)