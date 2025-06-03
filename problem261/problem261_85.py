S = input()
ctr = 0
for i in range (len(S)//2):
    A,B = S[i], S[-1-i]
    if A != B:
        ctr += 1
print(ctr)