x,n = map(int,input().split())
if n == 0:
    print(x)
else:
    L = list(map(int,input().split()))
    ans = []
    cur = 0
    while len(ans) == 0:
        temp_1 = x-cur
        temp_2 = x+cur
        if temp_1 not in L:
            ans.append(temp_1)
        if temp_2 not in L:
            ans.append(temp_2)
        cur += 1
    print(ans[0])
