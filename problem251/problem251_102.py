n,k = list(map(int,input().split()))
r,s,p = list(map(int,input().split()))
t = str(input())

t_list = []

for i in range(k):
  t_list.append(t[i])

for i in range(k,n):
  if t[i] != t_list[i-k] or t_list[i-k] == 'all':
    t_list.append(t[i])
  else:
    t_list.append('all')

print(t_list.count('r') * p + t_list.count('s') * r + t_list.count('p') * s)
