def show(nums):
    for i in range(len(nums)):
        if i != len(nums) - 1:
            print(nums[i],end=' ')
        else:
            print(nums[i])

def bubbleSort(A,N):
    flag = 1
    count = 0
    while flag:
        flag = 0
        for j in range(N-1,0,-1):
            if A[j] < A[j-1]:
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp
                flag = 1
                count += 1
    show(A)
    print(count)

N = int(input())
A = list(map(int,input().split()))


bubbleSort(A,N)

