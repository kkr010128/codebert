cnt = [0 for i in range (26)]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
str = open(0).read()
for x in str:
    for k in range(len(alphabet)):
        if x == alphabet[k] or x == alphabet[k].upper():
            cnt[k] = cnt[k] + 1
            break

for i in range(26):
    print(alphabet[i], ':', cnt[i])
