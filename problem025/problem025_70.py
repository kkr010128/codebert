n = int(input())
a = list(map(int,input().split()))
m = int(input())
q = list(map(int,input().split()))
cand = []
for i in range(2**n):
    tmp = 0
    for j in range(n):
        if(i>>j)&1:
            tmp += a[j]
    if tmp not in cand:
        cand.append(tmp)
for i in q:
    print('yes' if i in cand else 'no')
