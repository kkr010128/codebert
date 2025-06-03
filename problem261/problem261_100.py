S = input()
S_inv = S[-1::-1]
counter = 0
for i in range(len(S)//2):
    if S[i]!=S_inv[i]:
        counter +=1
print(counter)
