import math

H = int(input())
count = 0
atk = 0
for i in range(10 ** 12):
   
    if H == 1:
        for j in range(0,atk+1):
            count += 2 ** j
        break
    else:
        H = math.floor(H / 2)
        atk += 1

print(count) 