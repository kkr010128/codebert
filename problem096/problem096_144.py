n, d = map(int, input().split())
x = [0 for i in range(n)]
y = [0 for i in range(n)]
for i in range(n):
    x[i],y[i] = map(int, input().split())
cnt = 0
for i in range(n):
    dis = x[i]*x[i] + y[i]*y[i]
    if(dis<=d*d):
        cnt+=1
print(cnt)