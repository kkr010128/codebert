n = int(input())
a = list(map(int, input().split()))
q = int(input())
bc = [list(map(int, input().split())) for i in range(q)]
l = [0] * 100000
suml = 0
for i in a:
  l[i-1] += 1
  suml += i
for i in bc:
  suml += l[i[0]-1] * (i[1] - i[0])
  l[i[1]-1] += l[i[0]-1]
  l[i[0]-1] = 0
  print(suml)