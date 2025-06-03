N, M = map(int, input().split())
t_ans = []
for _ in range(M):
  t_ans.append(list(map(str,input().split())))

ans_num = [0]*(N+1)
ans_pe = [0]*(N+1)

for i in range(M):
  result = t_ans[i][1]
  question = int(t_ans[i][0])
  if result == 'AC' and ans_num[question] == 0:
    ans_num[question] = 1
  elif result == 'WA' and ans_num[question] == 0:
    ans_pe[question] += 1

for i in range(N+1):
  if ans_num[i] != 1:
    ans_pe[i] = 0

print(f'{sum(ans_num)} {sum(ans_pe)}')