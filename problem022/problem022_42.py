n = input()

S = [int(x) for x in raw_input().split()]

q = input()

T = [int(x) for x in raw_input().split()]

C = 0

for i in T:
 for j in S:
  if i==j:
   C += 1
   break

print C