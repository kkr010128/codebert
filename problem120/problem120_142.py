#template
def inputlist(): return [int(j) for j in input().split()]
#template
N,K = inputlist()
p = inputlist()
p.sort()
ans = 0
for i in range(K):
    ans +=p[i]
print(ans)