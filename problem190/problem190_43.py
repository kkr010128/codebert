import sys
S=list(input())
reverse_S = S[::-1]

if S==reverse_S:
    for i in range(int(len(S)/2)):
        if S[i]==S[int(len(S)/2)-i-1] and S[int(len(S)/2)+1+i]==S[len(S)-1-i]:
            continue
        else:
            print("No")
            sys.exit()
    print("Yes")
else:
    print("No")
