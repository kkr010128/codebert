n = int(raw_input())

points = [0, 0]
for i in xrange(n):
  card_list = raw_input().split(" ")
  if card_list[0] > card_list[1]:
    points[0] += 3
  elif card_list[0] < card_list[1]:
    points[1] += 3
  else:
    points[0] += 1
    points[1] += 1

print str(points[0]) + " " + str(points[1])