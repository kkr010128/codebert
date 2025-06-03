N, R = (int(x) for x in input().split())
if N >= 10:
  result = R
else:
  result = R + 100*(10-N)
print(result)