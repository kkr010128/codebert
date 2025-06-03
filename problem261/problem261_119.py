s = input()
if len(s) == 1:
    print('0')
else:
    if len(s) % 2 == 0:
        sa = s[:len(s)//2]
        sb = s[len(s)//2:]
        sbr = sb[::-1]
    else:
        sa = s[:(len(s)-1)//2]
        sb = s[(len(s)-1)//2:]
        sbr = s[::-1]
    n = 0
    for i in range(len(sa)):
        if sa[i] != sbr[i]:
            n += 1
    print(n)