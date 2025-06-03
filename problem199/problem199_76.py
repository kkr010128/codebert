S = input()
List1= []
List2 = []
n1 = 0
n2 = 0
for i in range(0,len(S),2):
  List1.append(S[i])
for i in range(1,len(S),2):
  List2.append(S[i])
n1 = List1.count("h")
n2 = List2.count("i")
if n1 == len(List1) and n2 == len(List2) and n1 == n2:
  print("Yes")
else:
  print("No")
