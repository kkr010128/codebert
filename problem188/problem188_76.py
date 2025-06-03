X, Y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
p_sum = [0]*(a+1)
q_sum = [0]*(b+1)
for i in range(a):
    p_sum[i+1] = p_sum[i] + p[i]
for i in range(b):
    q_sum[i+1] = q_sum[i] + q[i]
#print(p_sum)
#print(q_sum)
ans = [0]*(c+1)
ans[0] = p_sum[X] + q_sum[Y]
x, y = X, Y
flag = True
for i in range(c):
    if x > 0 and y > 0:
        ans[i+1] = max(ans[i]-p[x-1]+r[i], ans[i]-q[y-1]+r[i], ans[i])
        if ans[i+1] == ans[i]-p[x-1]+r[i]:
            x -= 1
        elif ans[i+1] == ans[i]-q[y-1]+r[i]:
            y -= 1
        elif ans[i+1] == ans[i]:
            break
    elif x == 0:
        ans[i+1] = max(ans[i]-q[y-1]+r[i], ans[i])
        if ans[i+1] == ans[i]:
            break
        else:
            y -= 1
    elif y == 0:
        ans[i+1] = max(ans[i]-p[x-1]+r[i], ans[i])
        if ans[i+1] == ans[i]:
            break
        else:
            x -= 1
    elif x == 0 and y == 0:
        flag = False
if flag:
    print(max(ans))
else:
    print(sum(r[:x+y-1]))
