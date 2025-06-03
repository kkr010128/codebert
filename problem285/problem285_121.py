S = input()
INC = '<'
DEC = '>'
icnt = 0
dcnt = 0
mode = DEC
ans = 0
for c in S:
  if mode == DEC:
    if c == DEC:
      dcnt += 1
    elif c == INC:
      if icnt <= dcnt:
        ans += (dcnt + 1) * dcnt // 2
      else:
        ans += icnt + dcnt * (dcnt - 1) // 2
      icnt = 1
      mode = INC
  elif mode == INC:
    if c == INC:
      icnt += 1
    elif c == DEC:
      ans += icnt * (icnt - 1) // 2
      dcnt = 1
      mode = DEC
if mode == INC:
  ans += (icnt + 1) * icnt // 2
elif mode == DEC:
  if icnt <= dcnt:
    ans += (dcnt + 1) * dcnt // 2
  else:
    ans += icnt + dcnt * (dcnt - 1) // 2
print(ans)