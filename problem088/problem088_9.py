N = int(input())
A = [int(i) for i in input().split()]

count = 0
for i in range(N) :
    if i==0 :
        continue
    if A[i]<A[i-1] :
        count += abs(A[i]-A[i-1])
        A[i] += abs(A[i]-A[i-1])

print(count)