K = int(input())
S = input()
i = 0
string = ""
if len(S) > K:
    while i < K:
        string += S[i]
        i += 1
    print(string + "...")
else:
    print(S)