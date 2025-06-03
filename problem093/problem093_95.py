n,k = map(int, input().split())
p = [0]+[int(x) for x in input().split()]
c = [0]+[int(x) for x in input().split()]

ans=-10**18

for saisyo in range(1,n+1):
    tensuulist=[]
    genzaiti=saisyo

    while(True):
        genzaiti=p[genzaiti]
        tensuulist.append(c[genzaiti])
        if genzaiti==saisyo:
            break

    goukei=sum(tensuulist)
    nagasa=len(tensuulist)
    kaisuu=k
    syou=kaisuu//nagasa
    amari=kaisuu%nagasa

    tensuu=0
    nokorikaisuu=0

    if goukei<=0:
        for i in range(nagasa):
            tensuu+=tensuulist[i]
            ans=max(ans,tensuu)
    else:
        if 3*nagasa<kaisuu:
            tensuu+=goukei*(syou-1)
            nokorikaisuu=nagasa+amari
            for i in range(nokorikaisuu):
                tensuu+=tensuulist[(i%nagasa)]
                ans=max(ans,tensuu)
        else:
            for i in range(kaisuu):
                tensuu+=tensuulist[(i%nagasa)]
                ans=max(ans,tensuu)

print(ans)