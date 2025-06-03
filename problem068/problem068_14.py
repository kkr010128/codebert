word=''
com = ""
a = 0
b = 0
word=str(raw_input())
num=int(raw_input())
for i in range(num):
    add= raw_input().split()
    com = add[0]
    a = int(add[1])
    b = int(add[2])
    if com == 'replace':
        word = word[0:a] + add[3] + word[b+1:]
       # word = word.replace(word[a:b+1],add[3])
    elif com == 'reverse':
        tmp = word[a:b+1]
        word = word[0:a] + tmp[::-1] + word[b+1:]
    elif com == 'print':
        print word[a:b+1]
    else :
        break