a,b,c,d,e = map(int, input().split())
list = [a,b,c,d,e]
for i in range(5):
  if list[i] == 0:
    print(i+1)