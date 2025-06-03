a = raw_input().lower()
s = 0
while True:
    b = raw_input()
    if b == 'END_OF_TEXT':
        break
    b = b.split()
    b = map(str.lower,b)
    s += b.count(a)
print s