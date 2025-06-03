n = int(input())

output = ""
for i in range(1,n+1):
    if i % 3 == 0:
        output += " %s" % (i,)
        continue
    elif i % 10 == 3:
        output += " %s" % (i,)
        continue
    x = i
    while x > 1:
      x = int(x/10)
      if x % 10 == 3:
        output += " %s" % (i,)
        break
print(output)