x=input()
ret = ''
for a in x:
    if a.islower() : a = a.upper()
    elif a.isupper(): a = a.lower()
    ret += a
print(ret)