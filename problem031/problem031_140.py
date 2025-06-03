import math
while 1:
    n=int(input())
    if n==0:
        break
    ave=0.0
    aru=0.0
    m=[float(i) for i in input().split()]
    for i in range(n):
        ave=ave+m[i]
    ave=ave/n
    for i in range(n):
        aru=aru+(m[i]-ave)*(m[i]-ave)
    aru=math.sqrt(aru/n)
    print("%.5f"% aru)