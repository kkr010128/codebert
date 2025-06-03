N = int(input())
S, T = input().split()
s_list = list(S)
t_list = list(T)
ans = ''
for i in range(N):
  ans += s_list[i]
  ans += t_list[i]
print(ans)