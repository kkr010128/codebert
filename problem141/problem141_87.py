N = int(input())
A = list(map(int, input().split()))

if N == 0 and A[0] == 1:
    print(1)
    exit()

if A[0] != 0:
    print(-1)
    exit()
    
sum_leaf = sum(A)
ans = 1
before_top = 1
for i in range(1, len(A)):
    if A[i] <= before_top*2:
        ans += min(sum_leaf, before_top*2)
        before_top = min(sum_leaf, before_top*2) - A[i]
        sum_leaf -= A[i]
    else:
        print(-1)
        exit()

print(ans)