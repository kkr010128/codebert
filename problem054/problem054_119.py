count = int(raw_input())
S = []
H = []
C = []
D = []

while count:
  arr = map(str, raw_input().split(" "))
  if arr[0] == "S":
    S.append(int(arr[1]))
  elif arr[0] == "H":
    H.append(int(arr[1]))
  elif arr[0] == "C":
    C.append(int(arr[1]))
  else:
    D.append(int(arr[1]))
  count -= 1

S.sort()
H.sort()
C.sort()
D.sort()

ans_s = []
ans_h = []
ans_c = []
ans_d = []

for x in range(1, 14):
  if not x in S:
    ans_s.append(x)
  if not x in H:
    ans_h.append(x)
  if not x in C:
    ans_c.append(x)
  if not x in D:
    ans_d.append(x)

def answer(arr, value):
  for x in arr:
    print "%s %s" % (value, str(x))

answer(ans_s, 'S')
answer(ans_h, 'H')
answer(ans_c, 'C')
answer(ans_d, 'D')