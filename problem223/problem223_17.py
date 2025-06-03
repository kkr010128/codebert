n,k = map(int,input().split())
p = list(map(int,input().split()))

pp = list(map(lambda x:(x+1)/2,p))

p_rui = [pp[0]]
for i in range(1,n):
    p_rui.append(p_rui[i-1]+pp[i])



walist=[p_rui[k-1]]
for i in range(0,n-k):
    walist += [p_rui[k+i]-p_rui[i]]

print(max(walist))


