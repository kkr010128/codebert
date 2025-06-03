x,y,a,b,c = map(int, input().split())
li_p = list(map(int, input().split()))
li_q = list(map(int, input().split()))
li_r = list(map(int, input().split()))
li_p.sort(reverse=True)
li_q.sort(reverse=True)
li_r.sort(reverse=True)
r = []
for i in range(x):
  r.append(li_p[i])
for i in range(y):
  r.append(li_q[i])
for i in range(c):
  r.append(li_r[i])
r.sort(reverse=True)
print(sum(r[:x+y]))
