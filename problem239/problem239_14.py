s = 'abcdefghijklmnopqrstuvwxyz'
c = input()
for i in range(26):
    if c == s[i]:
        print(s[i+1])
        exit()
exit()