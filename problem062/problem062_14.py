# -*-coding:utf-8

def main():

    while True:
        inputNumber = input()
        if(inputNumber == '0'):
            break
        else:
            print(sum(list(map(int, inputNumber))))

if __name__ == '__main__':
    main()