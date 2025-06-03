x, y, a, b, c = map(int, input().split())

p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
q.sort(reverse=True)

eat_list = []

for i in range(x):
    eat_list.append(p[i])
for i in range(y):
    eat_list.append(q[i])
for i in range(c):
    eat_list.append(r[i])
    
eat_list.sort(reverse=True)

ans = 0

for i in range(x+y):
    ans += eat_list[i]

print(ans)