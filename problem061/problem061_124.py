s = input()
ss = ''

for i in s:
    if i.islower():
        l = i.upper()
    elif i.isupper():
        l =i.lower()
    else: l = i
    ss += l
print(ss)
