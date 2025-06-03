n = int(input())
a = list(map(int, input().split()))
x = 0
for a_i in a:
  x ^= a_i
for a_i in a:
  print(x ^ a_i)