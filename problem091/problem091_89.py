import itertools

input()
rods = list(map(int, input().split(" ")))
sorted_rods = sorted(rods)

count = 0
for combination in itertools.combinations(sorted_rods, 3):
  a, b, c = combination
  if a != b and b != c:
    if a + b > c:
      count += 1
      
print(count)