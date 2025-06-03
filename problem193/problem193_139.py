n, m, k = [int(i) for i in input().split()]

subsets = []
splits = [i for i in range(1, n)]
n -= 1
for i in range(2**n):
    x = []
    for j in range(n):
        if i&(1<<j):
            x.append(j)
    subsets.append(x)
n+=1
A = []
for i in range(n):
    A.append([int(j) for j in input()])
ans = n*m
for subset in subsets:
    cur_ans = len(subset)
    tmp = []
    col = 0
    subset.append(100000)
    running_sum = [0 for i in range(len(subset))]    
    while col<m:
        row_ptr = 0    
        for row in range(n):
            if row > subset[row_ptr]:
                row_ptr += 1
            running_sum[row_ptr] += A[row][col]
            if running_sum[row_ptr] > k:
                col -= 1
                running_sum = [0 for i in range(len(subset))]
                cur_ans += 1
                break
                
        col += 1                
        if cur_ans >= ans:
          break
    ans = min(ans, cur_ans)
print(ans)
