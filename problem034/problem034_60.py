diceA = list(map(int, input().split()))

diceB = [[1,2,3,5,4,2],[2,1,4,6,3,1],[3,1,2,6,5,1],[4,1,5,6,2,1],[5,1,3,6,4,1],[6,2,4,5,3,2]]

q = int(input())

for i in range(q):
  quest = list(map(int, input().split()))
  ans = 0
  for j in range(6):
    if quest[0] == diceA[j]:
      for k in range(6):
        if quest[1] == diceA[k]:
          for l in range(1,5):
            if diceB[j][l] == k+1:
              ans = diceB[j][l+1]
  print(diceA[ans-1])
