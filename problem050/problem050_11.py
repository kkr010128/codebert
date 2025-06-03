while True:
    [h,w] = map(int,input().split())
    if h==0 and w ==0: break
    s = ['#'*w+'\n', (('#' + '.'*(w-2) + '#')[0:w]+'\n')*(h-2), '#'*w+'\n' ]
    t = list(filter(lambda x: x!='', s))
    print(''.join(t[0:h]))