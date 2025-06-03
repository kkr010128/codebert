import string
text = ''
while True:
    try:
        text += input().lower()
    except EOFError:
        break
for chr in string.ascii_lowercase:
    print('{} : {}'.format(chr, text.count(chr)))
