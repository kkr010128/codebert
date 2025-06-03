S = input()
if len(S) %2 == 1:
  print("No")
  exit()
for i in range(len(S)):
  if S[i] != "hi"[i%2]:
    print("No")
    exit()
print("Yes")