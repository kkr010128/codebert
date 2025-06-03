S = input()

s1 = S[0:int((len(S)-1)/2)]
s2 = S[int((len(S)/2))+1:len(S)+1]
if S == S[::-1] and s1 == s1[::-1] and s2 == s2[::-1]:
    print("Yes")
else:
    print("No")