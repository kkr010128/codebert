n = int(input())
l = list(map(int, input().split()))
ans=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for h in range(j+1,n):
            if l[i] != l[j] and l[i] != l[h] and l[j] != l[h]:
                mnum = max(l[i],l[j],l[h])
                if mnum < l[i] + l[j] + l[h] - mnum:
                    ans+=1
print(ans)