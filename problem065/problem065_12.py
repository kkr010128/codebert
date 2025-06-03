w = input().lower()
text = ''
while True:
    t = input()
    if t == 'END_OF_TEXT':
        break
    text += t.lower() + ' '
print(len([t for t in text.split(' ') if t == w]))