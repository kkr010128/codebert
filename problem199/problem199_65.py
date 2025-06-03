s = input()
a = 0
if(len(s)%2 == 1):
    print('No')
else:
    for i in range(len(s)//2):
        if(s[2*i] != 'h' or s[2*i+1] != 'i'):
            a = 1
            print('No')
            break
    if(a == 0):
        print('Yes')