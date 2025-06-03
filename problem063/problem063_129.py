import sys
def lower(word):
    Word = ''
    str = list(word)
    for i in range(len(str)):
        if str[i].isupper(): Word += str[i].lower()
        else: Word += str[i]
    return Word
a = []
for line in sys.stdin:
    a.extend(list(line))


count = [0] * 26
for i in range(len(a)):
    a[i] = lower(a[i])
    if 97 <= ord(a[i]) and ord(a[i]) < 123:
        count[ord(a[i]) - 97] += 1
for i in range(26):
    print(chr(i + 97) + ' : ' + str(count[i]))

