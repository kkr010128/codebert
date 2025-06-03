_ = input()
S = input()
newS = S.replace("ABC", "")
print((len(S) - len(newS)) // 3)