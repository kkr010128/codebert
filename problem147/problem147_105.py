
S = input()
T = input()
s = len(S)
for i in range(s):
    if S[i] == T[i]:
        continue
    else:
        print('No')
        exit()
print("Yes")
