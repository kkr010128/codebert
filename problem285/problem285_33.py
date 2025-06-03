s = input().strip()

buf = s[0]
count = 0
popa  = []
suma = 0
for i in s:
  if i=="<":
    count+=1
    suma += count
  elif i==">" and buf=="<":
    popa.append(count)
    suma -= count
    count = 0
  buf = i
buf = s[-1]
count = 0
dupa  = []
for i in s[::-1]:
  if i==">":
    count+=1
    suma += count
  elif i=="<" and buf==">":
    dupa.append(count)
    suma -= count
    count = 0
  buf = i

for i,j in zip(dupa[::-1],popa):
  suma+=max(i,j)
print(suma)
# print(sum(map(int,"0 3 2 1 0 1 2 0 1 2 3 4 5 2 1 0 1".split())))
