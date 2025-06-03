# 21   import sympyが最速だが、Atcoderには無い
import math
x = int(input())

#エラトステネスの篩
n = [i for i in range(2,int(math.sqrt(x))+1)]

for i in n:
    for j in n:
        if j % i == 0 and j/i !=1:
            n.remove(j)
            
while x > 0:
    for i in n:
        if x % i == 0:
            break
    else:
        print(x)
        break
    x+=1