n = int(input())

y =list(map(int,input().split()))
x = list()

for i in range(n-1,-1,-1):
    arry = y[i]
    x.append(arry)

for i in range(n):
    if(i == n-1):
        print('{}'.format(x[i]))
    else:
        print(x[i],end=' ')
    
