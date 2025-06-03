def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())
import sys
sys.setrecursionlimit(10**6)

s=input()
if s[2]==s[3] and s[4]==s[5]:
    print("Yes")
else:
    print("No")