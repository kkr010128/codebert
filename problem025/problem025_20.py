n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

cand_list = []
for i in range(1, 2**n):
    cum_num=0
    for j in range(n):
        if i&1<<j:
            cum_num += A[j]
    cand_list.append(cum_num)
    
for m in M:
    if m in set(cand_list):
        print('yes')
    else:
        print('no')
