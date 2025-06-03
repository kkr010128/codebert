A,B = map(int, input().split())

tmp_A, tmp_B = max(A,B), min(A,B)

while 1:
  if tmp_A % tmp_B != 0:
    tmp = tmp_B
    tmp_B = tmp_A%tmp_B
    tmp_A = tmp
  else:
    if tmp_B == 1:
      result = A*B
      break
    else:
      result = int(A*B/tmp_B)
      break
print(result)