A, B = map(int, input().split())
times = A * B
if A < B:
  A, B = B, A
while B > 0:
  temp = A % B
  A = B
  B = temp
print(int(times/A))