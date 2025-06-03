n = list(raw_input())

for i in xrange(len(n)):
    if n[i].isupper(): n[i]=n[i].lower()
    elif n[i].islower(): n[i]=n[i].upper()
print ''.join(n)