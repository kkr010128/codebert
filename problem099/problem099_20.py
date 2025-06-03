N, K = map(int,input().split())
A = list(map(int,input().split()))
start = 0
end = 10**9
while end - start > 1:
   l = (start + end)/2
   l = int(l)
   count = 0
   for i in range(N):
      q = A[i]/l
      if q == int(q):
         q -= 1
      count += int(q)
   if count <= K:
      end = l
   else:
      start = l
print(end)