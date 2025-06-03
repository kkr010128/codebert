N = int(input())
A = list(map(int, input().split()))

money = 1000
stock = 0

for i in range(N-1) :
  if A[i] > A[i+1] :
    money += stock * A[i]
    stock = 0
  elif A[i] < A[i+1] :
    temp = int(money / A[i])
    stock += temp
    money -= temp * A[i]
    
money += stock * A[N-1]
stock = 0
print(money)