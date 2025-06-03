import itertools as it

n, A = int(input()), [*map(int, input().split())]
yes_nums = set()
for bools in it.product([True, False], repeat=n):
  yes_nums.add(sum(A[i] for i in range(n) if bools[i]))

_ = input()
for m in map(int, input().split()):
  print("yes" if m in yes_nums else "no")
