word = input()
text = []
count = 0

while True:
    line = input()
    if line=='END_OF_TEXT':
        break
    else:
        text.append(line.lower().split())


for i in text:
    for j in i:
        if j == word:
            count += 1

print(str(count))