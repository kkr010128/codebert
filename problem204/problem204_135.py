S = str(input())
Q = int(input())
flip = 0
front,back = '',''
for i in range(Q):
  j = input()
  if len(j) == 1:
    flip += 1
    continue
  else:
    if j[2] == '1' and flip % 2 == 0:
      front = j[4] + front
      continue
    elif j[2] == '2' and flip % 2 == 0:
      back = back + j[4]
      continue
    elif j[2] == '1' and flip % 2 ==1:
      back= back + j[4]
      continue
    elif j[2] == '2' and flip % 2 ==1:
      front = j[4] + front
      continue
S = front + S + back
if flip % 2 == 1:
  S = S[::-1]
print(S)