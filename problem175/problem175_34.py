n = int(input())
s = input()

total = s.count("R") * s.count("G") * s.count("B")

#l = ["RGB", "RBG", "GRB", "GBR", "BRG", "BGR"]

lR = [0]*n
lG = [0]*n
lB = [0]*n

for i in range(len(s)):
    if s[i] == "R":
        lR[i] += 1
    elif s[i] == "G":
        lG[i] += 1
    else:
        lB[i] += 1

#print(lR)
#print(lG)
#print(lB)

for i in range(n):
    j = 1
    if lR[i]:
        while i-j >= 0 and i+j < n:
            if lG[i+j]!=0 and lG[i+j] == lB[i-j]:
                total -= 1
            elif lG[i-j]!=0 and lG[i-j] == lB[i+j]:
                total -= 1
            j += 1

    elif lG[i]:
        while i-j >= 0 and i+j < n:
            if lR[i+j]!=0 and lR[i+j] == lB[i-j]:
                total -= 1
            elif lR[i-j]!=0 and lR[i-j] == lB[i+j]:
                total -= 1
            j += 1

    elif lB[i]:
        while i-j >= 0 and i+j < n:
            if lG[i+j]!=0 and lG[i+j] == lR[i-j]:
                total -= 1
            elif lG[i-j]!=0 and lG[i-j] == lR[i+j]:
                total -= 1
            j += 1

print(total)
