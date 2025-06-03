while True:
    try:
        spam=map(int, input().split(' '))
        spam = [i for i in spam]
        spam.sort()
        cola = spam[0] * spam[1]
        while True:
            if spam[0] == 0:
                print('{} {}'.format(spam[1],int(cola/spam[1])))
                break
            pre = spam[0]
            spam[0] = spam[1] % spam[0]
            spam[1] = pre
    except:
        break