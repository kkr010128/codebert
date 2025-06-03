S = input()
N = int(len(S))

S1 = S[:int(N/2)]
S2 = S[int(N/2)+1:N]
#print(S1)
#print(S2)

for i in range(int(N/2)):
    if(S[i] != S[N-1-i]):
        print("No")
        exit()

    if(S1[i] != S1[int(N/2)-1-i]):
        print("No")
        exit()

    if(S2[i] != S2[int(N/2)-1-i]):
        print("No")
        exit()

print("Yes")        