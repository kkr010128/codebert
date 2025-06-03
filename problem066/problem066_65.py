#9_2
def shuffle(letter,num):
    for i in range(num):
        memory=''
        h=int(input())
        bellow=letter[0:h]
        above=letter[h:len(letter)]
        memory=above+bellow
        letter=memory
    return letter

##main##
while(True):
    letter=input()
    if(letter in "-"):
        break
    else:
        num=int(input())
        letter=shuffle(letter,num)
        print(letter)
