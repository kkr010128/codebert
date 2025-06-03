w = input().lower()
cnt = 0
while 1:
  l = input().split()
  if "END_OF_TEXT" in l: break
  for e in l:
    if e.lower() == w: cnt += 1
print(cnt)
