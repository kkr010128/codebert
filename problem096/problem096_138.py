N ,D = map(int , input().split())
sum = 0
for i in range(N):
    a,b = map(int , input().split())
    if(((a ** 2 + b ** 2)**(1/2)) <= D):
        sum += 1
print(sum)