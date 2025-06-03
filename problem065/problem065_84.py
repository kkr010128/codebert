target = raw_input()
count = 0
while True:
    line = raw_input()
    if  line == 'END_OF_TEXT':
        break
    if line[-1] == '.':
        line = line[:-1]
    for word in line.lower().split():
        if target == word:
            count += 1
print count