n = int(input())
x_i = [float(i) for i in input().split()]
y_i = [float(i) for i in input().split()]
abs_sub = []
D1,D2,D3=0.0,0.0,0.0
for i in range(len(x_i)):
#p==1
    D1 += ((x_i[i]-y_i[i])**2)**(1/2)
#p==2
    D2 +=(x_i[i]-y_i[i])**2
#p==3
    D3 +=(((x_i[i]-y_i[i])**2)**(1/2))**3
#p==inf
    abs_sub.append(((x_i[i]-y_i[i])**2)**(1/2))
D2 = D2**(1/2)
D3 = D3**(1/3)
D_inf=abs_sub[0]
for i in range(len(abs_sub)):
    if D_inf < abs_sub[i]:
        D_inf = abs_sub[i]
print("{:.6f}\n{:.6f}\n{:.6f}\n{:.6f}".format(D1,D2,D3,D_inf))
