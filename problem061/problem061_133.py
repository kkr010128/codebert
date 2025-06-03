import string
a = raw_input()
b = ""
for i in range(len(a)):
    if a[i] in string.ascii_lowercase :
        b = b + a[i].upper()
    elif a[i] in string.ascii_uppercase :
        b = b + a[i].lower()
    else :
        b = b + a[i]

print b