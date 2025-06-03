from itertools import product

N = int(input())
A = [None] * N
lst = [[] for _ in range(N)]
for i in range(N):
    A[i] = int(input())
    lst[i] = [list(map(int, input().split())) for _ in range(A[i])]

bit_lst = list(product(range(2), repeat=N)) #N桁のビット

ans = 0
for bit in bit_lst:
    f = True #このbitの証言が無意味になったらFalse
    for a in range(N):
        #1人ずつ順番に聞く : a人目の証言
        if f:
            for b in range(A[a]):
                #b個目の証言
                if bit[a] == 1:
                    #この人が正直者なとき
                    if lst[a][b][1] != bit[lst[a][b][0]-1]:
                        #正直者の証言と現実が食い違う
                        f = False
                        break
                else:
                    #正直者ではないとき
                    break
    if f:
        ans = max(ans, sum(bit))
print(ans)