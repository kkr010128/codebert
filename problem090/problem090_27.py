s = input()
count = 0
for i in range(len(s)):
  if s[i] == "R":
    count += 1
    if i + 1 >= 3:
      break
    elif s[i+1] == "S":
      break
print(count)