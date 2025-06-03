palavra= input()
tam= len(palavra)
if palavra[tam-1]=='s':
    print(palavra+'es')
else:
    print(palavra+'s')