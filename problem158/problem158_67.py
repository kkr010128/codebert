K = int(input())
A,B = map(int, input().split())

lst = list(range(A, B + 1))

for i in lst:
  if(i % K == 0):
    print("OK")
    break
else:
  print("NG")