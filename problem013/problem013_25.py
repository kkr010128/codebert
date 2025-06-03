n = int(raw_input())
num_list = [int(raw_input()) for i in xrange(n)]

minv = num_list[0]
maxv = -1000000000

for i in xrange(1, n):
  tmp = num_list[i] - minv
  maxv = tmp if tmp > maxv else maxv
  minv = num_list[i] if minv > num_list[i] else minv
  # print "i = %d, tmp = %d, maxv = %d, minv = %d" % (i, tmp, maxv, minv)

print maxv