n, a, b = [int(i) for i in input().split()]
a_distance = a-1
b_distance = n-b
ab_distance = b - a

if ab_distance % 2 == 0:
  result = ab_distance//2
else:
  if a_distance < b_distance:
    result = a_distance + (ab_distance-1)//2 + 1
  else:
    result = b_distance + (ab_distance-1)//2 + 1
print(result)

