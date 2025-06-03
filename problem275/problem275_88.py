XY= list(map(int,input().split()))
X=XY[0]
Y=XY[1]

if X==1:
    syokinx=300000
elif X==2:
    syokinx=200000
elif X==3:
    syokinx=100000
else:
    syokinx=0

if Y==1:
    syokiny=300000
elif Y==2:
    syokiny=200000
elif Y==3:
    syokiny=100000
else:
    syokiny=0

if X==1 and Y==1:
    syokinz=400000
else:
    syokinz=0

print(syokinx+syokiny+syokinz)
