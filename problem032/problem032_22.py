n = int(input())
x = list(map(float, input().split(' ')))
y = list(map(float, input().split(' ')))
p1 = 0.0
p2 = 0.0
p3 = 0.0
pm = 0.0
i = 0
while i < n:
    p1 += abs(x[i] - y[i])
    p2 += pow(abs(x[i] - y[i]), 2)
    p3 += pow(abs(x[i] - y[i]), 3)
    pm = max(pm, abs(x[i] - y[i]))
    i += 1
p2 = pow(p2, 0.5)
p3 = pow(p3, 0.333333333333333)
ans = '{0:.8f}'.format(p1) + '\n'
ans += '{0:.8f}'.format(p2) + '\n'
ans += '{0:.8f}'.format(p3) + '\n'
ans += '{0:.8f}'.format(pm)
print(ans)
