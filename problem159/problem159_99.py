x = int(input())
cnt = 0
dep = 100
while True:
  dep = dep * 101 // 100
  cnt+= 1
  if dep >= x:
    print(cnt)
    break