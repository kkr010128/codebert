n = int(input())
A = list(map(int, input().split()))
A.sort()

l = [False]*(A[n-1] + 1)
fix = []
for i in A:
    if l[i]:
        fix.append(i)
    l[i] = True
    
for i in range(A[n-1]+1):
    if l[i]:
        for j in range(i*2, A[n-1]+1, i):
            l[j] = False

for i in fix:
    l[i] = False
    
ans = [i for i in range(A[n-1] + 1) if l[i]]

print(len(ans))
