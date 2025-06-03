H,A=map(int,input().split())
AP=0
for i in range(10001):
  AP=A*i
  if AP>=H:
    print(i)
    break