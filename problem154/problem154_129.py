n,k = map(int, input().split())
num = []

for i in range(k):
  d = int(input())
  num += list(map(int, input().split()))

Q = list(set(num))
print(n-len(Q))