i = str(input())
w =''
for let in i:
    if(let == let.upper()):
        w = w + let.lower()
    elif(let == let.lower()):
        w = w + let.upper()
    else:
        w = w + let
print(w)
