N = int(input())
line = [int(i) for i in input().split()]
sum = 1
line.sort(reverse=True)
if line[len(line) -1]== 0:
  print(0)
  exit()
for num in line:
  sum = sum * num
  if sum > 10 ** 18:
    print(-1)
    exit()
print(sum)