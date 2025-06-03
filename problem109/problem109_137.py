N = int(input())
A = [input() for _ in range(N)]
count = [0] * 4
for a in A:
  if a == 'AC':
    count[0] += 1
  elif a == 'WA':
    count[1] += 1
  elif a == 'TLE':
    count[2] += 1
  else:
    count[3] += 1

print(f"AC x {count[0]}")
print(f"WA x {count[1]}")
print(f"TLE x {count[2]}")
print(f"RE x {count[3]}")