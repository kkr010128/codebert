word = input().lower()
text = []
c = 0
while True:
    read = input().split()
    if read[0] == 'END_OF_TEXT':
        break
    else:
        text.append(read)
for i in text:
    for n in i:
        if word == n.lower():
            c += 1
print(c)