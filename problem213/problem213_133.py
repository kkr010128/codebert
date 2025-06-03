n = int(input())
x = list(map(int,input().split()))
ans = 1000000000000
for i in range(1,101):
    b = 0 
    for num in x:
        b += (num - i)**2
    ans = min(b,ans)

print(ans)
