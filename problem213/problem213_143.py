input()
l = list(map(int,input().split()))
l.sort()
ans = 1000000
n_ans = 0
for i in range(l[0],l[len(l)-1]+1):
  for j in range(len(l)):
    n_ans += (l[j]-i) ** 2
  if n_ans <= ans:
    ans = n_ans
    n_ans = 0
  else:
    n_ans = 0
print(ans)