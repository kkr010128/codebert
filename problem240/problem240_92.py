N,M=map(int,input().split())
List = []
for i in range (M):
  List.append(list(map(str, input().split())))
resList= [False]*N
res = 0
waList = [0]*N
for i in range(M):
  if resList[int(List[i][0])-1] == False:
    if List[i][1] == "AC":
      resList[int(List[i][0])-1] = True
      res += waList[int(List[i][0])-1] 
    else:
      waList[int(List[i][0])-1] += 1
print(resList.count(True),res)