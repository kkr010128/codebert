text = input()
tend = len(text)
text2 = ""
if text[len(text)-1:len(text)] == "s":
    text2 = text +'es'
else:
    text2 = text +'s'
print(text2) 
