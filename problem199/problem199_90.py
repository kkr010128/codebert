s = str(input())
#print(s[0]+s[1])

hitati = "hi"

for i in range(5):
  if s == hitati:
    print("Yes")
    exit()
  else:
    hitati += "hi"

print("No")