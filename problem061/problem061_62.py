n=raw_input()
a=''
for i in n:
    if i.islower():a+=i.upper()
    else:a+=i.lower()
print a