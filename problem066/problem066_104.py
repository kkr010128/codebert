def sub(strings, listseq):
    for index in listseq:
        strings = strings[index:] + strings[:index]
    return strings



def main():
    while True:
        strings = input()
        if strings == "-": break
        times = int(input())
        list1 = [int(input()) for i in range(times)]
        print(sub(strings, list1))



main()
