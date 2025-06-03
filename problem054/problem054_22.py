def az16():
    list = []
    n = input()
    for i in range(0,n):
        list.append(raw_input().split())
    for mark in ["S","H","C","D"]:
        for i in range(1,14):
            if [mark,repr(i)] not in list:
                print mark,i

az16()