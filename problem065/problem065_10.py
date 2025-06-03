w = str.lower(raw_input())
t = []
while True:
  line = raw_input()
  if line == "END_OF_TEXT":
    break
  else:
    t += (map(str.lower, line.split(" ")))

count = 0
for i in xrange(len(t)):
  if w == t[i]:
    count += 1

print count