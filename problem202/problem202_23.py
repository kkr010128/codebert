N, A, B = map(int, input().split())
M = N % (A+B)
cnt = (N // (A+B))*A
if M < A:
    print(cnt+M)
else:
    print(cnt+A)
