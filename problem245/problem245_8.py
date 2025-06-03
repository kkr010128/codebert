#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))

n = int(input())
s = input()

ans = 0
aDec = False
bDec = False

for i in range(n):
    if s[i] == "A":
        aDec = True
        bDec = False
    elif s[i] == "B":
        if (aDec):
            bDec = True
        else:
            bDec = False
        aDec = False
    elif s[i] == "C":
        if (bDec):
            ans += 1
        bDec = False
        aDec = False
    else:
        bDec = False
        aDec = False
print(ans)
