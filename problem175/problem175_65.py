n = int(input())
s = input()

sr = [] 
sg = []
sb = [0] * n
kcnt = 0
for i in range(n):
  if s[i] == 'R':
    sr.append(i)
  elif s[i] == 'G':
    sg.append(i)
  else:
    sb[i] = 1
    kcnt += 1

ans = 0
for i in sr:
  for j in sg:
    nki = j*2 - i
    nkj = i*2 - j
    nkk = (j+i)
    ans += kcnt
    if  0<= nki < n and sb[nki] == 1:
        ans -= 1
    if 0<= nkj < n and sb[nkj] == 1:
        ans -= 1
    if nkk%2 == 0 and 0<= (nkk//2) < n and sb[nkk//2] == 1:
      ans -= 1

print(ans)