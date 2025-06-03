import math

def getDistance(n, x, y, p):
  temp = 0.0
  for i in xrange(n):
    temp += math.fabs(x[i] - y[i]) ** p
    # print "temp = " + str(temp)
  temp2 = 1.0 / p
  # print temp2
  return math.pow(temp, temp2)


n = int(raw_input())
x = map(float, raw_input().split(" "))
y = map(float, raw_input().split(" "))

for i in xrange(1, 4):
  print "{0:.6f}".format(getDistance(n, x, y, i))

max = 0.0
for i in xrange(n):
  d = math.fabs(x[i] - y[i])
  if d > max:
    max = d

print "{0:.6f}".format(max)