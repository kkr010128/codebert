S = input()
s = len(S)
ct = 0
for i in range(s):
    if S[i] != S[(-i-1)]:
        ct += 1 
print(ct//2)
