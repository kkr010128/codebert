k = int(input())
a,b = map(int,input().split())

for i in range(1000):
  if a <= k*i <= b:
    print("OK")
    exit()
  elif b < k*i:
    print("NG")
    exit()