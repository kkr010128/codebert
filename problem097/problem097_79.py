n=int(input())
s=0
for i in range(n+1):
    s=(10*s+7)%n
    if(s==0):
        print(i+1)
        exit()
print(-1)

