
def main():
        
    N_satu, M_satu, K_fun = map(int, input().split())

    A_fun = list(map(int, input().split()))
    B_fun = list(map(int, input().split()))

    SumOf_A = [0]
    SumOf_B = [0]

    for i in range(N_satu):
        next_val = SumOf_A[i] + A_fun[i]
        SumOf_A.append(next_val)

    for i in range(M_satu):
        next_val = SumOf_B[i] + B_fun[i]
        SumOf_B.append(next_val)

    index_b = M_satu
    max_cnt = 0

    for i in range(N_satu + 1):
        if (SumOf_A[i] > K_fun):
            break
        
        while (SumOf_A[i] + SumOf_B[index_b] > K_fun):
            index_b -= 1
        
        max_cnt = max(max_cnt, i + index_b)
        

    print(max_cnt)


if __name__ == '__main__':
    main()
