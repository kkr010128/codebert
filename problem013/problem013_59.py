def maximumProfit(A, N):
    minR = A[0]
    minP = A[1] - A[0]
    for i in range(1, N):
        R = A[i] - minR
        if R > minP:
            minP = R
        if A[i] < minR:
            minR = A[i]
    return minP

if __name__ == "__main__":
    N = input()
    A = []
    for i in range(N):
        A.append(input())
    print maximumProfit(A, N)