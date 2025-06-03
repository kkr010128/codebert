N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

flag = True
c = 0
while flag:
    flag = False
    for j in reversed(range(1, N)):
        if  A[j - 1] > A[j]:
            A[j - 1],    A[j] = A[j], A[j - 1]
            c += 1
            flag = True
    
print(' '.join(map(str, A)))
print(c)