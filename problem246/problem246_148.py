import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

patterns = itertools.permutations(list(range(1, N+1)), N)
p_i = 0
q_i = 0
for i, ptn in enumerate(patterns):
  p_same = True
  q_same = True
  for j, num in enumerate(ptn):
    if P[j] != num:
      p_same = False
    if Q[j] != num:
      q_same = False
  if p_same:
    p_i = i
  if q_same:
    q_i = i
print(abs(p_i-q_i))