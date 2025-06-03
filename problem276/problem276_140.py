N = int(input())
A = list(map(int, input().split()))
Sum = 0
Temp = 0
for a in A:
    Sum += a
for i in range(N):
    Temp += A[i]
    if Temp > Sum//2:
        index = i
        break

print(min(abs(Sum-2*Temp), abs(Sum-2*(Temp-A[index]))))