value = input()
convert_value = []
for x in value:
    if x.isupper():
        convert_value.append(x.lower())
    elif x.islower():
        convert_value.append(x.upper())
    else:
        convert_value.append(x)
print(''.join(x for x in convert_value))