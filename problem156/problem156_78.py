X=int(input())

for A in range(1000):
  for B in range(-100, 1000):
    if A**5 - B**5 == X:
      ans = (A,B)

print(*ans)