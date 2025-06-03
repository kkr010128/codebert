n, k = map(int, input().split())
positions = [int(i) for i in input().split()]
scores = [int(i) for i in input().split()]
if max(scores) <= 0:
  print(max(scores))
else:
  positions = [0] + positions
  scores = [0] + scores
  max_point = -pow(10, 9)
  #print(max_point)
  dic = {}
  for i in range(1, n + 1):
    f_pos = i
    #print('f_pos',f_pos)
    if f_pos not in dic:
      point_loop = 0
      loop = 0
      pos_set = set([f_pos])
      while True:
        f_pos = positions[f_pos]
        point_loop += scores[f_pos]
        #print('pos', f_pos)
        #print(point)
        loop += 1
        if f_pos in pos_set:
          for j in pos_set:
            dic[j] = [loop, point_loop]
          break
        pos_set.add(f_pos)
    else:
      loop, point_loop = dic[f_pos]
    #print(loop, point)
    loop_c = k // loop
    r = k % loop
    if loop_c == 0 or point_loop <= 0:
      if point_loop <= 0:
        if loop_c > 0:
          r = loop
      point = 0
      for _ in range(r):
        f_pos = positions[f_pos]
        point += scores[f_pos]
        max_point = max(max_point, point)
    else:
      point1, point2 = 0, 0
      point1 = loop_c * point_loop
      max_point1 = point1
      for _ in range(r):
        f_pos = positions[f_pos]
        point1 += scores[f_pos]
        max_point1 = max(point1, max_point1)
      f_pos = i
      point2 = (loop_c - 1) * point_loop
      max_point2 = point2
      for _ in range(loop):
        f_pos = positions[f_pos]
        point2 += scores[f_pos]
        max_point2 = max(point2, max_point2)
      max_point = max(max_point, max(max_point1, max_point2))
  print(max_point)
