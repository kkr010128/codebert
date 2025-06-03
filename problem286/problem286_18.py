a,b = map(int,input().split())
li = []
for i in range(1,10):
    for j in range(1,10):
        if i==a and j == b:
            print(a*b)
            exit()
print(-1)