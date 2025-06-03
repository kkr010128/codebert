N = int(input())
x = input().strip()
cnt = 0
for i in range(N):
    if x[i]=="R":
        cnt += 1
if cnt==0 or cnt==N:
    print(0)
else:
    ans = 0
    for i in range(cnt):
        if x[i]=="W":
            ans += 1
    print(ans)