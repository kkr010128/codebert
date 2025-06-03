n = int(input())
n_li = list(map(int, input().split()))

q = int(input())
q_li = list(map(int, input().split()))

ans = [0]*q
tmp_li = []

for i in range(2**n):
    check = [0]*n
    
    for j in range(n):
        if ((i >> j) & 1):
            check[n - 1 - j] = 1
    
    tmp = 0
    for a in range(n):
        if check[a] == 1:
            tmp += n_li[a]
    tmp_li.append(tmp)

for k in range(q):
    if q_li[k] in tmp_li:
        ans[k] = 1
        
for x in ans:
    if x == 1:
        print('yes')
    else:
        print('no')
