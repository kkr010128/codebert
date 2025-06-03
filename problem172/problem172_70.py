def main():
    l = list(str(input()))
    num = len(l)
    for i in range(num):
        if l[i] == '7':
            print('Yes')
            return
    print('No')
main()