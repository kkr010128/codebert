n = int(input())
dic_A = set()
dic_C = set()
dic_G = set()
dic_T = set()
for i in range(n) :
    p, string = input().split()
    if p == 'insert' :
        if string[0] == 'A' :
            dic_A.add(string)
        elif string[0] == 'C' :
            dic_C.add(string)
        elif string[0] == 'G' :
            dic_G.add(string)
        else :
            dic_T.add(string)
    else :
        if string[0] == 'A' :
            if string in dic_A :
                print('yes')
            else :
                print('no')
        elif string[0] == 'C' :
            if string in dic_C :
                print('yes')
            else :
                print('no')
        elif string[0] == 'G' :
            if string in dic_G :
                print('yes')
            else :
                print('no')
        else :
            if string in dic_T :
                print('yes')
            else :
                print('no')
