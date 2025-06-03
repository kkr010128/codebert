N = int(raw_input())
A = map(int, raw_input().split())

counter = 0
while True:
  ischanged = False
  for i in xrange(1, N):
    if A[N-i] < A[N-i-1]:
      tmp = A[N-i]
      A[N-i] = A[N-i-1]
      A[N-i-1] = tmp
      counter += 1
      ischanged = True
  if ischanged == False:
    break
print " ".join(map(str, A))
print counter