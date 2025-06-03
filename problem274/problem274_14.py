n,m = map(int,input().split())
s = input()[::-1]
idx = 0
ans = [0]
while True:
    flg = False
    step = 0
    for i in range(1, m+1):
        if idx+i <= n:
            if s[idx+i]=='0':
                step = i
                flg = True
    if flg==False:
        break
    else:
        idx += step
    ans.append(idx)

if ans[-1]!=n:
    print(-1)
else:
    ret = []
    for i in range(1,len(ans)):
        ret.append(ans[i]-ans[i-1])
    print(*ret[::-1])