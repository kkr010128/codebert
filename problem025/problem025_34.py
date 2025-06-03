#Exhaustive Search (bit全探索ver)
n = int(input())
A = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

count_list = []
for i in range(1<<n):
    copy_A = A.copy()
    count = 0
    for j in range(n):
        mask = 1 << j
        if mask & i != 0:
            count += A[j]
    count_list.append(count)

for k in m:
    if k in count_list:
        print('yes')
    else:
        print('no')
    
