import random

def Nickname():

    Name = str(input()) #入力回数を決める

    num = random.randint(0, len(Name) - 3)

    print(Name[num:num+3])

if __name__ == '__main__':
    Nickname()