text = input()
newText = ""

for x in text:
    if x.isupper():
        newText = newText + x.lower()
    elif x.islower():
        newText = newText + x.upper()
    else:
        newText = newText + x
    
print(newText)