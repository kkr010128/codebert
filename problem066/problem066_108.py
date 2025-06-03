string = ''
while True:
    hoge = input().strip()
    if hoge == '-':
        print (string)
        break
    if hoge.isalpha():
        if string:
            print (string)
        string = hoge
        count = 0
    else:
        if count == 0:
            count = hoge
            continue
        else:    
            string = string[int(hoge):] + string[:int(hoge)]
