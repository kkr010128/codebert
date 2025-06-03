# 初期入力
from copy import copy
K = int(input())

#
lunlun_start =["1","2","3","4","5","6","7","8","9"]
lunlun_roop =copy(lunlun_start)
lunlun =[]
ans =copy(lunlun_start)
x=""
while len(ans) <K:
#for i in range(1,10):
    lunlun =[]
    for i in lunlun_roop:
        if i[-1] =="0":
            lunlun.append(i+"0")
            lunlun.append(i+"1")
        elif i[-1] =="9":
            lunlun.append(i+"8")
            lunlun.append(i+"9")
        else:
            x =int(i+i[-1])-1
            lunlun.append((str(x) ))
            x +=1
            lunlun.append((str(x) ))
            x +=1
            lunlun.append((str(x) ))
        if len(lunlun) >K:
            break
    lunlun_roop =copy(lunlun)
    ans.extend(lunlun)
print(ans[K-1])