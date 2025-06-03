n = int(input())

dic = {}
for i in range(1, 10):
  for j in range(1, 10):
    dic[(str(i), str(j))] = 0

for i in range(1, n+1):
  if i % 10 == 0:
    continue
  front = str(i)[0]
  back = str(i)[-1]
  dic[(front, back)] += 1
ans = 0
for i in range(1, 10):
  for j in range(1, 10):
    ans += dic[(str(i), str(j))] * dic[(str(j), str(i))]
print(ans)
