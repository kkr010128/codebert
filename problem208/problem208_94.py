n,m = map(int,input().split())
ans = ["num"]*n
for i in range(m):
    s,c = map(int,input().split())
    if ans[s-1] == "num" or ans[s-1] == c:
        ans[s-1] = c
    else:
        print("-1")
        exit()

if ans[0] == 0 and n >= 2:
    print("-1")
    exit()
elif ans[0] == 0 and n == 1:
    print("0")
    exit()
elif ans[0] == "num" and n == 1:
    print("0")
    exit()
elif ans[0] == "num":
    ans[0] = 1

for j in range(n):
    if ans[j] == "num":
        ans[j] = 0

[print(ans[k],end ="") for k in range(n)]