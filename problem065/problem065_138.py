W = input().lower()
count = 0
while True:
    l = input()
    if l == 'END_OF_TEXT':
        break
    for i in l.lower().split():
        if i == W:
            count += 1
print(count)