h = int(input())
ans = 1
num = 1
while h>1:
    h//=2
    num*=2
    ans+=num
print(ans)