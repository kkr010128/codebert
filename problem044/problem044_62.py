#! python3

a, b, c = [int(x) for x in input().strip().split(' ')]
r = 0
for i in range(a, b+1):
  if c % i == 0:
    r += 1
print(r)