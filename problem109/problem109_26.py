N = int(input())

S = [""]*N

Dict={}

ac=0
wa =0
tle =0
re=0


for i in range(N):
    S[i] = str(input())
    
for  j in S:
    if j in  Dict:
        temp = Dict[j]
        Dict[j] = temp + 1
    else:
        Dict[j] = 1
        
if "AC" in Dict:
    ac = Dict["AC"]
    
if "WA" in Dict:
    wa = Dict["WA"]
    
if "TLE" in Dict:
    tle = Dict["TLE"]
    
if "RE" in Dict:
    re = Dict["RE"]
    
    
print("AC x " , ac)
print("WA x " , wa)
print("TLE x " , tle)
print("RE x " , re)