num = list(map(int,input().split()))
c = 0
for i in range(num[0],num[1]+1):
    if(num[2]%i == 0): c = c+1

print(c)
