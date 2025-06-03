N = int(input())
Stones = list(input())

count_red = 0
count_white = 0

for i in range(N):
  if Stones[i] == "R":
    count_red += 1
    
for i in range(count_red):
  if Stones[i] == "W":
    count_white += 1
    
print(count_white)