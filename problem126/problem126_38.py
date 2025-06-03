n = list(map(int,input().split()))

num = 0
for i,x in enumerate(n):
    if (x == 0):
        num = i+1
        break;
print(num)