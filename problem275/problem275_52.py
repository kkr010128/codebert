s = input().split()
kane = int()
if int(s[0]) == 1:
  kane = kane + 300000
elif int(s[0]) == 2:
  kane = kane + 200000
elif int(s[0]) == 3:
  kane = kane + 100000
else:
  pass

if int(s[1]) == 1:
  kane = kane + 300000
elif int(s[1]) == 2:
  kane = kane + 200000
elif int(s[1]) == 3:
  kane = kane + 100000
else:
  pass
  
if int(s[0]) + int(s[1]) == 2:
  kane = 1000000

print(kane)