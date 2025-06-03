N = input()
check = False
for i in range(3):
  if N[i] == "7":
    check = True
    
print("Yes" if check else "No")