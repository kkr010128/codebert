n = int(input())
S = [int(x) for x in input().split()]
q = int(input())
T = [int(x) for x in input().split()]

count = 0
for target in T:
  if target in S:
    count += 1

print(count)