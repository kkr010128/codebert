import string
x = ''
allcase = string.ascii_lowercase
while True:
    try: x+=input().lower()
    except:break
for letter in allcase:
    print(letter + " : " + repr(x.count(letter)))