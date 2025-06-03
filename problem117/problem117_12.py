n, m, k = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
aa = [0]
bb = [0]
 
for s in range(n):
    aa.append(aa[s] + a[s])
for s in range(m):
    bb.append(bb[s] + b[s])      
ans = 0
j = m
 
for i in range(n+1):
    if aa[i] > k:
        break
    while bb[j] > k - aa[i]:
        j -= 1
    ans = max(ans, i+j)
        
print(ans)