import itertools

N, M, Q = map(int, input().split())

abcd_list = []
for q in range(Q):
    abcd_list.append(list(map(int, input().split())))

#print(abcd_list)
list_tmp = []
for i in range(1, M + 1):
    list_tmp.append(i)

comb_A = list(itertools.combinations_with_replacement(list_tmp, N))


max_score = 0
for A in comb_A:
    tmp_score = 0
    for q in range(Q):
        A_a = A[abcd_list[q][0] - 1]
        A_b = A[abcd_list[q][1] - 1]

        if(A_b - A_a == abcd_list[q][2]):
            tmp_score += abcd_list[q][3]
        
    max_score = max(max_score, tmp_score)

print(max_score)