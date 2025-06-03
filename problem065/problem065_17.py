text = ''

key= input().lower()
while True:
    s = input()
    if s.find("END_OF_TEXT") >= 0: break
    try:
        text += s + ' '
    except:
        break

print([x.lower() for x in text.split(" ")].count(key) )