S,T = open(0).read().split()
ls = len(S)
lt = len(T)
ans = float('inf')
for i in range(ls-lt+1):
    temp = S[i:i+lt]
    t2 = 0
    for j in range(lt):
        if temp[j] != T[j]:
            t2 += 1
    ans = min(ans,t2)
print(ans)