str = input()

if len(str)%2 == 1:
    print('No')
else:
    for i in range(0,len(str),2):
        moji = str[i:i+2]
        # print(moji)
        if moji != 'hi':
            ans = 1
            break
        else:
            ans = 0
    if ans==1:
        print('No')
    else:
        print('Yes')