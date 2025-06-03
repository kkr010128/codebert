S = list(str(input()))

for i in range(len(S)-1):
    if i == 0 and S[0] == '?':
        if S[i+1] == 'P':
            S[0] = 'D'
        else:
            S[0] = 'P'
    if S[i] == '?':
        if S[i+1] == 'P':
            S[i] = 'D'
        else:
            if S[i-1] == 'P':
                S[i] = 'D'
            else:
                S[i] = 'P'

if S[len(S)-1] == '?':
    S[len(S)-1] = 'D'

strS = "".join(S)

print(strS)