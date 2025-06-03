N = int(input())
S = input()
char = ''

for i in range(len(S)):
    char += chr((ord(S[i]) + N - 65) % 26 + 65)

print(char)
