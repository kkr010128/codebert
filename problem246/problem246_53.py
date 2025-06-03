from math import factorial

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))


def cnt(x):
  pattern = 0
  numbers = list(i for i in range(1, n+1))
  for i in range(n):
    if x[i] > min(numbers): 
      pattern += numbers.index(x[i]) * factorial(n-i-1)
    numbers.remove(x[i])
  return pattern


print(abs(cnt(p) - cnt(q)))