S = input()
T = input()
U = [0] * (len(S)-len(T)+1)
for j in range(len(S)-len(T)+1):
    for i in range(len(T)):
        if(S[i+j] != T[i]):
            U[j] += 1
print(min(U))