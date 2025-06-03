x = int(input())
a = x % 100
b = x // 100
cnt = 0
ans = 0

for i in [5,4,3,2,1]:
    cnt += a // i
    a %= i
    
if cnt <= b:
    ans = 1
    
print(ans)