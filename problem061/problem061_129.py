sentence = input()
for i in sentence:
    if i.isupper() == True:
        print(i.lower(), end = "")
    elif i.islower() == True:
        print(i.upper(), end = "")
    else:
        print(i, end = "")
print()
