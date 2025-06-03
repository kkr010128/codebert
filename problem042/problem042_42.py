list = []
x = 1
while x > 0:
    x = input()
    if x > 0:
        list.append(x)

for i,j in enumerate(list):
  print "Case " + str(i+1) + ": " + str(j)