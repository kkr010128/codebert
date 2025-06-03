N = int(raw_input())
A = map(int, raw_input().split())

def bubbleSort(A, N):
    count = 0
    flag = 1
    while flag:
        flag = 0
        for i in range(N-1, 0, -1):
            if A[i] < A[i-1]:
                temp = A[i]
                A[i] = A[i-1]
                A[i-1] = temp
                flag = 1
                count += 1
    return count

count = bubbleSort(A, N)

print " ".join(map(str, A))
print count