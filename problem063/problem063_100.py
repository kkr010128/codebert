import string
s = ''
while True:
    try:
        s += input().lower()
    except EOFError:
        break
for a in string.ascii_lowercase:
    print('{0} : {1}'.format(a, s.count(a)))