N = int(raw_input())
taro_point = 0
hanako_point = 0
for n in range(N):
  str_card = raw_input().split()
  if str_card[0] > str_card[1]:
    taro_point += 3
  elif str_card[0] < str_card[1]:
    hanako_point += 3
  else:
    taro_point += 1
    hanako_point += 1
print '%d %d' % (taro_point, hanako_point)