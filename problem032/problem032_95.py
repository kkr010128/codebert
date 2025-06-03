N = int(input())
x = input().split()
y = input().split()

x = [int(j) for j in x]
y = [int(z) for z in y]
d1 = 0
d2 = 0
d4 = []
d3 = 0
for i in range(N):
    d1 += abs(x[i]- y[i])
    d2 += (x[i]-y[i])**2
    d3 += abs(x[i]-y[i])**3
    d4.append(abs(x[i]- y[i]))
d2_root = d2**0.5
d3_root = d3**(1/3)
print('{:.08f}'.format(d1))
print('{:.08f}'.format(d2_root))
print('{:.08f}'.format(d3_root))
print('{:.08f}'.format(max(d4)))
