n = int(input())
c = 0
for i in range(1,n):
      if (i%2==1):
            c+=1
print("{0:.10f}".format(1-(c/n)))
