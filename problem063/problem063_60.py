al = 'abcdefghijklmnopqrstuvwxyz'
text = ''

while True:
    try:
        text += input().lower()
    except EOFError:
        break

for i in al:
    print('{} : {}'.format(i, text.count(i)))
