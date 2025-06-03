n = int(input())
S = list(map(int, input(). split()))
q = int(input())
T = list(map(int, input(). split()))

Sum = 0
for i in T:
  if i in S:
    Sum += 1
print(Sum)