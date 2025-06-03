def find(A):
    increase = []
    for i in range(len(A)-1):
        if A[i] <= A[i+1]:
            increase += [1]
        else:
            increase += [0]
    increase += [0]
    
    val = 1000
    hold = 0
    for i in range(len(increase)):
        if i==0:
            if increase[i] == 1:
                hold = val//A[i]
                val -= A[i]*hold
        else:
            if increase[i] == 1:
                if increase[i-1] == 0:
                    hold = val//A[i]
                    val -= A[i]*hold 
            else:
                if increase[i-1] == 1:
                    val += A[i]*hold
                    hold = 0
    return val
N = input()
A = list(map(int,input().strip().split()))
print(find(A))