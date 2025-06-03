w = input()
r = ''
for i in range(len(w)):
    c = str(w[i])
    if (w[i].islower()):
        c = w[i].upper()
    elif (w[i].isupper()):
        c = w[i].lower()
    r = r + c

print(r)

