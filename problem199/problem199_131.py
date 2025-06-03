S = input()

if len(S) % 2 != 0:
  print("No")
  exit(0)

for i in range(len(S) // 2):
  s = S[2 * i: 2 * (i + 1)]
  if s != "hi":
    print("No")
    exit(0)
    
print("Yes")