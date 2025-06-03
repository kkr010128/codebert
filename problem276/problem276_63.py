N = int(input())
A = list(map(int, input().split()))
sumlow = 0
sumhigh = 0
i = 0
j = N-1
while i<=j:
    if sumlow <= sumhigh:
        sumlow += A[i]
        i += 1
    else:
        sumhigh += A[j]
        j -= 1
print(abs(sumlow-sumhigh))
