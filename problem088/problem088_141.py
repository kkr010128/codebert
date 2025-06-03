N = int(input())
A = list(map(int, input().split()))
fumidai_list, A_after = [], 0

for count_a in range(len(A)):
    fumidai = 0

    if(A[count_a] >= A_after):
        A_after = A[count_a]
        fumidai_list.append(fumidai)

    elif(A[count_a] < A_after):
        fumidai = A_after - A[count_a]
        fumidai_list.append(fumidai)

print(sum(fumidai_list))
