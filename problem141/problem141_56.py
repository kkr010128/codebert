def main():
    n = int(input())
    A = list(map(int, input().split()))

    if n  == 0:
        if A[0] == 1:
            return 1
        else:
            return -1
    elif A[0] != 0:
        return -1
    
    bound = [0]*(n+1)
    bound[n] = A[n]
    for i in range(n-1, -1, -1):
        bound[i] = bound[i+1] + A[i]

    B = [0] * (n+1)
    for i in range(n+1):
        if i == 0:
            B[i] = 1
        else:
            above = (B[i-1] - A[i-1]) * 2
            if  (i < n and above <= 0) or above < 0:
                return -1
            B[i] = min(above, bound[i])
    if B[n] < A[n]:
        return -1
    # print('B: ', B)
    return sum(B)

print(main())