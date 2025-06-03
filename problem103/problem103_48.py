N = int(input())
A = list(map(int, input().split()))

mon = 1000
kabu = 0

for i in range(N-1):
  if A[i] <= A[i+1]:
    kabu, mon = divmod(mon, A[i])
    mon += kabu * A[i+1]
    
print(mon)