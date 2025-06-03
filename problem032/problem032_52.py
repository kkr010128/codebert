import decimal
d = int(input())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

D_1 = 0
for i in range(d):
    L_i = abs(x[i] - y[i])
    D_1 += L_i

D_2 = 0
for i in range(d):
    L_i = abs(x[i]-y[i])**2
    D_2 += L_i
D_2 = (D_2) **(1/2)

D_3 = 0
for i in range(d):
    L_i = abs(x[i]-y[i])**3
    D_3 += L_i
D_3 = (D_3) ** (1/3)

L =[]
for i in range(d):
    L.append(abs(x[i]-y[i]))

D_ = max(L)

print('{:.8f}'.format(D_1))
print('{:.8f}'.format(D_2))
print('{:.8f}'.format(D_3))
print('{:.8f}'.format(D_))

