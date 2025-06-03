S = input()
T = input()
S_chars = list(S)
T_chars = list(T)
i = 0
count = 0


for roop in S_chars:
    if not S_chars[i] == T_chars[i]:
        count += 1
    i += 1
print(count)