w = input()
t = []
count = 0
while True:
    line = input()
    if line == 'END_OF_TEXT':
        break

    for x in line.split():
        if w.lower() == x.lower():
            count += 1
print(count)