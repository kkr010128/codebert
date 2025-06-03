Dict = set()
n = int(input())
for i in range(n):
 C = input().split()
 if C[0] =="insert":
  Dict.add(C[1])
 else:
  if C[1] in Dict:
   print("yes")
  else:
   print("no")