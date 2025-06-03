import math
H = int(input())
cnt = 0
monster = 1
while(H >= 1):
    cnt += monster
    H = math.floor(H/2)
    monster *= 2
print(cnt)