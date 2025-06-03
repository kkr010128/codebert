import math
N, A, B = map(int, input().split())
if math.log10(N)>math.log10(A+B)+100:
    print(A*(10**100))
elif N % (A+B) <= A:
    print((N//(A+B)*A)+(N%(A+B)))
else:
    print((N//(A+B)*A)+A)