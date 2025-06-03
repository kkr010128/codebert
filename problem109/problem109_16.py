listSi = [0,0,0,0]
ic = int(input())
icz = 0
while True:
  icz += 1
  i = input()
  if i == "AC":
    listSi[0] += 1
  elif i == "WA":
    listSi[1] += 1
  elif i == "TLE":
    listSi[2] += 1
  elif i == "RE":
    listSi[3] += 1
  if icz == ic:
    break
print(f"AC x {listSi[0]}")
print(f"WA x {listSi[1]}")
print(f"TLE x {listSi[2]}")
print(f"RE x {listSi[3]}")
