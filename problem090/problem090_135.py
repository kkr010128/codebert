s = list(input())

days = 0
if s[1] == "R":
  days += 1
  if s[0] == "R":
    days += 1
  if s[2] == "R":
    days += 1
    
else:
  if s[0] == "R" or s[2] == "R":
    days = 1
    
print(days)