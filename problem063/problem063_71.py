s1 = ''
try:
    while True:
        t = input()
        if t == '':
            break
        s1 += t
except EOFError:
    pass

n = [0] * 26
s = s1.lower()
for i in range(len(s)):
    j = ord(s[i]) - 97
    if j >= 0 and j < 26:
        n[j] += 1
for i in range(26):
    print('%s : %d' %(chr(i + 97),n[i]))
