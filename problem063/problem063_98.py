text = ''
while True:
    try:
        s = input().lower()
    except EOFError:
        break
    if s == '':
        break
    text += s
for i in 'abcdefghijklmnopqrstuvwxyz':
    print(i+' : '+str(text.count(i)))
    #print("{0} : {1}".format(i, text.count(i)))