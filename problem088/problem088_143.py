N = int(input())
A = list(map(int,input().split()))
sum_height = 0
max_height = A[0]
for i in range(1,len(A)):
    if A[i] < max_height:
        sum_height += max_height - A[i]
    else:
        max_height = A[i]
print(sum_height)

