x, y = map(int, input().split(" "))
 
total = 0
 
rewards = {1: 300000, 2: 200000, 3: 100000}

x1 = rewards[x] if (x <= 3) else 0
y1 = rewards[y] if (y <= 3) else 0
 
if (x == 1 and y ==  1):
  total += 400000
if (x1 != None):
  total += x1
if (y1 != None):
  total += y1
 
print(total)