n,m = map(int,input().split())
t = [[] for _ in range(n)]
for i in range(m):
    t_1,t_2 = map(int,input().split())
    t[t_1-1].append(t_2)

ans = ""
for i in range(n):
    if len(set(t[i])) == 1:
        ans += str(t[i][0])
    elif not t[i]:
        if i == 0:
            if n == 1:
                ans += "0"
            else:    
                ans += "1"
        else:
            ans += "0"
    else:
        print(-1)
        exit()
if ans[0] == "0":
    if n == 1:
        print(0)
    else:
        print(-1)
else:
    print(ans)
