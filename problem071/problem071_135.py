S = str(input())
if S[len(S)-1] == "s":
    S += "es"
else:
    S += "s"
print(S)