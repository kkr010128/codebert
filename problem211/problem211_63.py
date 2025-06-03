N,R = (int(x) for x in input().split())
if N<10:
    Ins = R+100*(10-N)
else:
    Ins = R
print(Ins)