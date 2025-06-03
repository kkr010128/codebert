N,D = map(int,input().split())
count = 0
for i in range(N):
    x,y = map(int,input().split())
    d = (x**2+y**2)**(1/2)
    if d <= D:
        count += 1
print(count)