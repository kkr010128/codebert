import math
n = int(input())
cnt = 0
for i in range(n):
    num = int(input())
    flag = True
    for j in range(2, int(math.sqrt(num))+1):
        if num%j == 0:
            flag = False
            break
    if flag:
        cnt+=1
print(cnt)