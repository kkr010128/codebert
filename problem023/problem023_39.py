dict = {}
n = int(raw_input())
for _ in xrange(n):
  com, word = raw_input().split()
  if com == "insert":
    dict[word] = True
  else:
    if word in dict:
      print "yes"
    else:
      print "no"