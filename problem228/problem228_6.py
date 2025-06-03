# D - Caracal vs Monster
H = int(input())

def rec(x):
    if x==1:
        return 1
    return 2*rec(x//2)+1

print(rec(H))