n = int(raw_input())

i = 0
s = []
h = []
c = []
d = []

def order_list(list):
  l = len(list)
  for i in xrange(l):
    j = i + 1
    while j < l:
      if list[i] > list[j]:
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
      j += 1

  return list

def not_enough_cards(mark, list):
  list = order_list(list)
  # line = "########################################"
  # print line
  # print mark + ":"
  # print list
  # print line
  i = 0
  for x in xrange(1, 14):
    # print "x = " + str(x) + ", i = " + str(i)
    if i >= len(list):
      print mark + " " + str(x)
    elif x != list[i]:
      print mark + " " + str(x)
    else:
      i += 1

while i < n:
  line = raw_input().split(" ")
  line[1] = int(line[1])
  if line[0] == "S":
    s.append(line[1])
  elif line[0] == "H":
    h.append(line[1])
  elif line[0] == "C":
    c.append(line[1])
  elif line[0] == "D":
    d.append(line[1])
  i += 1

not_enough_cards("S", s)
not_enough_cards("H", h)
not_enough_cards("C", c)
not_enough_cards("D", d)