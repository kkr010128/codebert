S = input()

result = 0
if "R" in S:
  if "RR" in S:
    result = S.count("R")
  else:
    result = 1

print(result)
