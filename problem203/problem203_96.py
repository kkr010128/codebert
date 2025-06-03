#C
A, B =map(int,input().split())

import math
price=[]
for i in range(10100):
    if math.floor(i*0.08)==A and math.floor(i*0.1)==B:
         price.append(i)
if len(price)==0:
    print(-1)
else:
    print(sorted(price)[0])