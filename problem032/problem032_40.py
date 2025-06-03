n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))
p_1 = sum([abs(x[i]-y[i]) for i in range(n)])
p_2 = (sum([(x[i]-y[i])**2 for i in range(n)]))**0.5
p_3 = (sum([(abs(x[i]-y[i]))**3 for i in range(n)]))**(1/3)
p_inf = max([abs(x[i]-y[i]) for i in range(n)])

print("{:.5f}".format(p_1))
print("{:.5f}".format(p_2))
print("{:.5f}".format(p_3))
print("{:.5f}".format(p_inf))