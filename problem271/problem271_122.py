N = int(input())
S = input()
T = ""
char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(S)):
    for j in range(26):
        if S[i] == char[j]:
            T += char2[j + N]
            break
print(T)
