N, M = map(int, input().split())
progress = {}
# initialize
for i in range(N):
  progress[str(i+1)] = ["notCorrect",0]
correct = 0

for i in range(M):
  question, result = map(str, input().split())
  if (progress[question][0] == "notCorrect"):
    if (result == "WA"):
      progress[question][1] += 1
    else:
      progress[question][0] = "correct"
      correct += 1
  else:
    continue
penalty = 0
for i in range(N):
  if (progress[str(i+1)][0] == "correct"):
    penalty += progress[str(i+1)][1]
print(str(correct)+" "+str(penalty))