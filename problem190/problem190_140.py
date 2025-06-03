S = input()
L = len(S)
for i in range((L-1)//2):
    if S[i] != S[L-1-i]:
        print("No")
        exit()

for i in range((L-1)//4):
    if S[i] != S[(L-1)//2-1-i]:
        print("No")
        exit()

for i in range(L-1, L - (L-1)//4, -1):
    if S[i] != S[i - (L-1)//2-1]:
        print("No")
        exit()

print("Yes")