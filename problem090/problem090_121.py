s = input()
rd = 0
max_rd = 0
for i in range(len(s)):
    if s[i] == 'R':
        rd += 1
        if max_rd < rd:
            max_rd = rd
    else:
        rd = 0
print(max_rd)