K=int(input())
S=input()
list1=[]
if len(S)<=K:
  print(S)
else:
  for i in range(K):
    list1.append(S[i])
  list1.append("...")
  S2="".join(list1)
  print(S2)