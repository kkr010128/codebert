X,Y,A,B,C = map(int,input().split())
AList = sorted(list(map(int,input().split())),reverse=True)
BList = sorted(list(map(int,input().split())),reverse=True)
CList = sorted(list(map(int,input().split())),reverse=True)
FullList = sorted(AList[:X] + BList[:Y])
counter = 0
for i in range(min(C,X+Y)):
  if CList[i] <= FullList[i]:
    break
  else:
    counter += 1
ans = sum(CList[:counter])+sum(FullList[counter:])
print(ans)
