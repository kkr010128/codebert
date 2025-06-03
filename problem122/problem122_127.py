N = int(input())
As = list(map(int, input().split()))
Q = int(input())
 
sumAs = 0
dictAs = [0] * 100000
for i in range(len(As)):
  sumAs += As[i]
  dictAs[As[i] - 1] += 1


for _ in range(Q):
  b, c = map(int, input().split())
  sumAs += dictAs[b - 1] * (c - b)
  dictAs[c - 1] += dictAs[b - 1]
  dictAs[b - 1] = 0
  print(sumAs)