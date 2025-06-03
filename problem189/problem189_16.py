N, M = map(int, input().split())

if N <= 1: a = 0
else: a = N*(N-1) // 2

if M <= 1: b = 0
else: b = M*(M-1) // 2
  
print(a+b)