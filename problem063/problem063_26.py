docs = ''
while True:
    try:
        s = raw_input()
    except:
        break
    docs += s.lower()
for ascii_num in range(97, 123):
    print '%s : %d' % (chr(ascii_num), docs.count(chr(ascii_num)))