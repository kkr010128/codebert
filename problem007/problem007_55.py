y=[1,1]
n=int(input())
for i in range(0,n):
    a=y[i]+y[i+1]
    y.append(a)
print(y[n])
