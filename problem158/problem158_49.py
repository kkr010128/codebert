K = int(input())
AB = input().split()
A = int(AB[0])
B = int(AB[1])

if int(B / K) * K >= A:
  print("OK")
else:
  print("NG")