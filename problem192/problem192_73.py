N = int(input())
A = [-1] + list(map(int, input().split()))

lis = [0]*(N+1)
for a in A[1:]:
    lis[a] += 1

sum_combinations = 0
for x in lis[1:]:
    if x >= 2:
        sum_combinations += x*(x-1)//2

for i in range(1,N+1):
    ans = sum_combinations
    num = lis[A[i]]
    if num >= 2:
        ans += (num-1)*(num-2)//2 - num*(num-1)//2
    
    print(ans)