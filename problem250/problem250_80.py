X = int(input())
res = X
j = 0
Flags = []
flg = True
for i in range(2,X+1):
  j = i+i
  flg = True
  while flg:
    Flags.append(j)
    if j > X:
      flg = False
    j += i
while res in Flags:
  res += 1
print(res)