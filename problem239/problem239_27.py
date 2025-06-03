letters = 'abcdefghijklmnopqrstuvwxyz'
c = input("")
res = ""
for i in range(len(letters)):
  if c == letters[i]:
    res+=letters[i + 1]
print(res)