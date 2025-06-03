n,k = list(map(int,input().split()))
point = list(map(int,input().split()))
rsp = ['r', 's', 'p']
t = input()
m = [rsp[rsp.index(i)-1] for i in t]
ans = 0
for i in range(n):
    if i<k :
        ans += point[rsp.index(m[i])]
    else:
        if m[i]!=m[i-k]:
            ans += point[rsp.index(m[i])]
        else:
            try:
                m[i] = rsp[rsp.index(m[i+k])-1]
            except:
                pass
    # print(ans)
print(ans)