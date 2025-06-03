import math
n = int(input())
dept=100
for i in range(n):
    dept=dept*1.05
    #print dept
    dept=math.ceil(dept)
    #print dept
print "%i"%(dept*1000)