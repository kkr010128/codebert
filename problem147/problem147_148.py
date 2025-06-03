s = input()
t = input()

for i in range(len(s)):
  if not s[i] == t[i]:
    print("No")
    exit()
    
print("Yes")