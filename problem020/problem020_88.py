n = input()
lis = []
bot = 0
for i in xrange(n):
    com = raw_input()
    if   com[0] == 'i':
        lis.append(com[7:])
    elif com[6] == ' ':
        try:
            lis.pop(~lis[::-1].index(com[7:]))
        except:
            pass
    elif com[6] == 'F':
        lis.pop()
    else:
        bot += 1

print ' '.join( map(str, reversed(lis[bot:])) )