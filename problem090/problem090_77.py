s = input()

ans = 0
strek = 0
for i in range(3):
  if s[i] == 'R':
    tmp = "R"
    strek += 1
    ans = max(strek, ans)
  else:
    strek = 0
    
print(ans)