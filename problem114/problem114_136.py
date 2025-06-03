import sys
readline = sys.stdin.readline

D = int(readline())
C = list(map(int,readline().split()))
S = [None] * D
for i in range(D):
  s = list(map(int,readline().split()))
  S[i] = s
  
def calc_score(arr):
  point = 0
  last_submit = [-1] * 26
  for i in range(len(arr)):
    point += S[i][arr[i]]
    last_submit[arr[i]] = i
    for j in range(len(last_submit)):
      point -= (i - last_submit[j]) * C[j]
    print(point)
  return point

T = [None] * D
for i in range(D):
  T[i] = int(readline()) - 1
  
ans = calc_score(T)
