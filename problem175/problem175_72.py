N = int(input())
S = list(input())
R = []
G = []
B = [0 for _ in range(N)]
b_cnt = 0
for i in range(N):
  if S[i] == 'R':
    R.append(i)
  elif S[i] == 'G':
    G.append(i)
  else:
    B[i] = 1
    b_cnt += 1
answer = 0
for r in R:
  for g in G:
    answer += b_cnt
    if (g-r)%2 == 0 and B[(r+g)//2] == 1:
      answer -= 1
    if 0 <= 2*g-r < N and B[2*g-r] == 1:
      answer -= 1
    if 0 <= 2*r-g < N and B[2*r-g] == 1:
      answer -= 1
print(answer)