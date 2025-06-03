def isKaibun(ss):    
    return ss==ss[::-1]

s = input()
ans=True
n=len(s)

if not isKaibun(s):
    ans=False
if not isKaibun(s[:((n-1)//2)]):
    ans=False

if ans:
    print("Yes")
else:
    print("No")
