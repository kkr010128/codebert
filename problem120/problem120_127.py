N, K= map(int, input().strip().split())
p = list(map(int, input().strip().split()))

p=sorted(p)
q=0
for i in range(K):
    q=q+p[i]

print(q)
