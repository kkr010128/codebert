A, B, C, D = map(int, input().split())

result = False

while A > 0 and C > 0:
  C -= B
  if C <= 0:
    result = 'Yes'
    break
  A -= D
  if A <= 0:
    result = 'No'
    break

print(result)