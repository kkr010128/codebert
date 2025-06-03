N = int(input())
ac = 0
wa = 0
tle = 0
re = 0
for _ in range(N):
  a = input()
  if a == "AC":
    ac += 1
  if a == "WA":
    wa += 1
  if a == "TLE":
    tle += 1
  if a =="RE":
    re += 1
print(f"AC x {ac}")
print(f"WA x {wa}")
print(f"TLE x {tle}")
print(f"RE x {re}")