def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

n=int(input())
ar=[]
for _ in range(n):
    ar.append(input())
from collections import Counter
c=Counter(ar)
print("AC x",c["AC"])
print("WA x",c["WA"])
print("TLE x",c["TLE"])
print("RE x",c["RE"])