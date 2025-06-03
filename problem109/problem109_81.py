N=int(input())
d={"AC":0,"WA":0,"TLE":0,"RE":0}
for _ in range(N):
    d[input()]+=1
print("AC x",d["AC"])
print("WA x",d["WA"])
print("TLE x",d["TLE"])
print("RE x",d["RE"])
