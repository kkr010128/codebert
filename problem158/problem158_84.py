K = input()
NUM = list(map(int,input().split()))
count = 0
for num in range(NUM[1]-NUM[0]+1):
  if ((NUM[0]+num )% int(K) == 0):
    print("OK")
    count += 1
    break

if (count == 0):
  print("NG")