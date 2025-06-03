#B - Mix Juice
N,K = map(int,input().split())
p = list(map(int,input().split()))
p_sorted = sorted(p,reverse = False)
ans = sum(p_sorted[:K])
print(ans)