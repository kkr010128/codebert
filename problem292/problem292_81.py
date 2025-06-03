n = int(input())
q = list(map(int,input().split()))
ans = 0

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        ans += q[i] * q[j]
    
print(ans//2)