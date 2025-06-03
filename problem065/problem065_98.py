W, c = input(), 0
for line in iter(input, 'END_OF_TEXT'):
    for Ti in  line.lower().split():
        if W == Ti:
            c +=1
print(c)