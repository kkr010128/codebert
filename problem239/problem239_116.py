alpha = "abcdefghijklmnopqrstuvwxyz"
s = input()
for i in range(len(alpha)):
    if alpha[i] == s:
        print(alpha[i+1])
        exit()
