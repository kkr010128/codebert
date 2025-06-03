N = int(input())
S = int(N**(1/2))
for i in range(S,0,-1):
    if N%i == 0:
        A = N//i
        B = i
        break

print(A+B-2)