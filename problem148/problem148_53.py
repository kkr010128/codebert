
a,b,c,k = map(int,input().split())
ans = min(a,k)
k -= ans
if k == 0:
    print(ans)
    exit(0)
k -= min(b,k)
if k == 0:
    print(ans)
    exit(0)
ans -= min(c,k)
print(ans)