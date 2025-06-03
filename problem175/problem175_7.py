n = int(input())
S = input()
rs = [s=="R" for s in S]
gs = [s=="G" for s in S]
bs = [s=="B" for s in S]

ind_r = [i for i,s in enumerate(rs) if s == 1]
ind_g = [i for i,s in enumerate(gs) if s == 1]
ind_b = [i for i,s in enumerate(bs) if s == 1]

ans = 0
ng = sum(gs)
for i in ind_r:
    for j in ind_b:
        # print(i,j)
        kM = max(i,j) + abs(i-j)
        km = min(i,j) - abs(i-j)
        ans += ng
        if (max(i,j) - min(i,j))%2==0:
            # print("aaa",(max(i,j)+min(i,j))//2)
            ans -= gs[(max(i,j)+min(i,j))//2]
        if kM < n:
            ans -= gs[kM]
        if 0 <= km:
            ans -= gs[km]
print(ans)