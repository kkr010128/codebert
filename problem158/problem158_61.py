x = int(input())
a, b = map(int, input().split())
for i in range(a, b+1):
  if i%x == 0:
    print("OK")
    break
  elif i == b:
    print("NG")