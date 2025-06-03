import sys,math

n=0
max_v=-math.pow(10,10)
s=math.pow(10,10)
for line in sys.stdin:
    l=int(line)
    if n == 0:
        n=l
        continue
    diff=l-s
    if diff>max_v:
        max_v=diff
    if diff<0:
        s=l
        

print max_v