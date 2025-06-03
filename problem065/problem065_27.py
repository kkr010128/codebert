def upper(word):
    Word = ''
    str = list(word)
    for i in range(len(str)):
        if str[i].islower(): Word += str[i].upper()
        else: Word += str[i]
    return Word

key_word = str(upper(input()))
sen = []
count = 0
while True:
    a = str(input())
    if a == 'END_OF_TEXT': break
    a = upper(a)
    sen.extend(a.split())
for i in range(len(sen)):
    if sen[i] == key_word:
        count+= 1
print(count)
