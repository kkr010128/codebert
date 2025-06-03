N, A, B = map(int, input().split())

a = N//(A+B)
b = N%(A+B)
if b > A:
    b = A
ans = a*A + b

print(ans)