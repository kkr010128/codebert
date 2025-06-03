import math
score = list(map(int,input().split()))
minut = score[2]*60 + score[3]
jisin = math.radians(minut/2)
hunsin = math.radians(score[3]*6)
jixy = [math.cos(jisin)*score[0] , math.sin(jisin)*score[0]]
huxy = [math.cos(hunsin)*score[1] , math.sin(hunsin)*score[1]]

delx = abs(jixy[0] - huxy[0])
dely = abs(jixy[1] - huxy[1])

answer = (delx**2 + dely**2)**0.5
print(answer)