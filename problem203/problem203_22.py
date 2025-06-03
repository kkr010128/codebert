import math
A,B=map(int,input().split())
eight=[]
i=0
ten=[]
for a in range(1,1001):
    if math.floor(a*0.08)==A:
        eight.append(a)
    if math.floor(a*0.1)==B:
        ten.append(a)

for a in eight:
    if a in ten:
        print(a)
        i=1
        break
if i==0:
    print("-1")
