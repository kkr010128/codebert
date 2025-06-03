numbers_a = []
numbers_b = []
character = []

while True:
  a,op,b = input().split()
  if op == "?":
    break
  a = int(a)
  b = int(b)
  numbers_a.append(a)
  numbers_b.append(b)
  character.append(op)

for i in range(len(character)):
  
  if character[i] == "+" :
    x = numbers_a[i] + numbers_b[i]
    
  if character[i] == "-":
    x = numbers_a[i] - numbers_b[i]
    
  if character[i] == "*":
    x = numbers_a[i] * numbers_b[i]
    
  if character[i] == "/":
    x = numbers_a[i] // numbers_b[i]
    
  print(x)
