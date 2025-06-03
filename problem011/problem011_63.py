def Euclidean(input_list):
  # print input_list
  x = input_list[1]
  y = input_list[0]
  r = x % y
  if r != 0:
    list = [r, y]
    list.sort()
    return Euclidean(list)
  else:
    return y

list = map(int, raw_input().split(" "))
list.sort()
print Euclidean(list)