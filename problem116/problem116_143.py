A = str(input())
B = str(input())
sum=0
for i in range(len(A)):
    if A[i]!=B[i]:
        sum+=1
print(sum)