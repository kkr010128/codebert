import math
A,B = map(int,input().split())
ans = 0
AT = 0.08
BT = 0.1

a = A/AT
b = B/BT
aPlus = (A+1)/AT
bPlus = (B+1)/BT

if a == b :
    ans = a
elif a < b :
    if aPlus <= b :
        ans = -1
    else :
        ans = b
elif b < a :
    if bPlus <= a :
        ans = -1
    else :
        ans = a

# print(a,b)
# print(aPlus,bPlus)
print(math.ceil(ans))