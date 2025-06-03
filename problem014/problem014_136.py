N = int(raw_input())
A = raw_input().split(" ")
count = 0
flag = 1

i = 0
while flag == 1:
    flag = 0
    for j in reversed(range(i+1, N)):
        if int(A[j]) < int(A[j-1]):
            temp = A[j]
            A[j] = A[j-1]
            A[j-1] = temp
            count += 1
            flag = 1
    i += 1
    
print " ".join(A)
print count