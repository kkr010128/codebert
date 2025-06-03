n = int(input())
a = [int(i) for i in input().split()]
b = []
sum_a = sum(a)
cum = 0
for i in a:
  cum += i
  b.append(abs(sum_a  - cum * 2))
print(min(b))