n = int(input())

alp = [chr(i) for i in range(97, 97+26)]

def dfs(i):
    if i == 1:
        return [("a", 1)]
    else:
        ret = []
        for i in dfs(i-1):
            nowstr, nowmax = i
            for j in range(nowmax+1):
                ret.append((nowstr+alp[j], max(j+1,nowmax)))
        return ret

ans = dfs(n)
#print(ans)
for i in range(len(ans)):
    print(ans[i][0])