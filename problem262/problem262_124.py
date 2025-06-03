import itertools

N = int(input())

H = []
for n in range(N):
    A = int(input())
    tmp = []
    for a in range(A):
        tmp.append(list(map(int, input().split())))
    H.append(tmp)
ans = 0 
for pro in itertools.product([0, 1], repeat=N):
    flag = 0
    for p in range(len(pro)):
        if pro[p] != 0:
            for h in H[p]:
                if pro[h[0]-1] != h[1]:
                    flag = 1
                    break
        if flag == 1:
            break
        if p == len(pro) - 1:
            ans = max(ans, sum(pro))

print(ans)


