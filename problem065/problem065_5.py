W = input()
num = 0
while True:
    line = input()
    if line == 'END_OF_TEXT':
        break
    for word in line.split():
        if word.lower() == W.lower():
            num += 1
print(num)