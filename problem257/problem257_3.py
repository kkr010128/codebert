n = int(input())
an = list(map(int, input().split()))
num = 1
for i in an:
    if i == num:
        num +=1
if num == 1:
    print(-1)
    exit(0)
ans = 1+n-num
print(ans)