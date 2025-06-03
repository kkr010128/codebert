s = input()
t = input()

# S_r = ''.join(list(reversed(S)))
cont = 0

for i in range(len(s)):
    if s[i] == t[i]:
        cont += 1

print(len(s)-cont)